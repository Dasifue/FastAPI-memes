"FastAPI routers and endpoints"

from fastapi import APIRouter, HTTPException, Form, File, UploadFile
from sqlalchemy.sql.schema import Sequence

from services.database import session
from services.minio_storage import upload_file, delete_file

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

    upload_file(file)    
    meme = MemeCreationSchema(
        title=title,
        file=file.filename,
    )
    return await MemeCRUD.create(
        meme=meme,
        async_session=session,
    )


@router.put("/{id}", response_model=MemeSchema)
async def update_meme(
    id: int,
    title: str | None = Form(None),
    file: UploadFile = File(...),
):
    "Endpoint for updating meme"

    meme = await MemeCRUD.get_one(
        meme_id=id,
        async_session=session,
    )
    if meme is None:
        raise HTTPException(status_code=404, detail="Meme not found")

    
    delete_file(file_name=meme.file)
    upload_file(file=file)

    return await MemeCRUD.update_by_instance(
        meme=meme,
        async_session=session,
        title=title,
        file=file.filename,
    )


@router.delete("/{id}", response_model=dict)
async def delete_meme(id: int) -> dict[str, str]:
    "Endpoint for meme deleting"
    meme = await MemeCRUD.get_one(
        meme_id=id,
        async_session=session,
    )
    if meme is None:
        raise HTTPException(status_code=404, detail="Meme not found")

    delete_file(file_name=meme.file)
    await MemeCRUD.delete_by_instance(
        meme=meme,
        async_session=session,
    )
    return {"detail": "deleted"}
