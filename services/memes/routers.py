"FastAPI routers and endpoints"

from fastapi import APIRouter, HTTPException, Form, File, UploadFile
from sqlalchemy.sql.schema import Sequence
from minio.error import S3Error

from services.database import session
from services.minio_storage import client

from .models import Meme
from .manager import MemeCRUD
from .schemas import MemeSchema, MemeCreationSchema


router = APIRouter(
    prefix="/memes",
    tags=["Memes"]
)

@router.get("/", response_model=list[MemeSchema])
async def get_memes(skip: int = 0, limit: int = 100) -> Sequence[Meme]:  # type: ignore
    "Endpoint returns array of memes"
    return await MemeCRUD.get_many(
        async_session=session,
        skip=skip,
        limit=limit,
    )

@router.get("/{id}", response_model=MemeSchema)
async def get_meme(id: int) -> Meme:
    "Endpoint returns one meme instance"
    meme = await MemeCRUD.get_one(
        async_session=session,
        meme_id=id,
    )
    if meme is None:
        raise HTTPException(status_code=404, detail="Meme not found")
    return meme

@router.post("/", response_model=MemeSchema)
async def create_meme(
    title: str = Form(...),
    file: UploadFile = File(...)
) -> Meme | dict[str, str]:
    "Endpoint for meme creation"
    try:
        client.put_object(
            bucket_name="memes",
            object_name=file.filename,
            data=file.file,
            length=file.size,
            content_type=file.content_type
        )
    except S3Error as error:
        return {"detail": str(error)}

    meme = MemeCreationSchema(
        title=title,
        file=file.filename,
    )
    return await MemeCRUD.create(
        meme=meme,
        async_session=session,
    )
