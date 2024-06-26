"FastAPI routers and endpoints"

from fastapi import APIRouter, HTTPException
from sqlalchemy.sql.schema import Sequence

from services.database import session

from .models import Meme
from .manager import MemeCRUD
from .schemas import MemeSchema


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
