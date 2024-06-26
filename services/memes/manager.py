"Base crud operations for meme model"

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy.sql.schema import Sequence
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select

from .models import Meme
from .schemas import MemeSchema

class MemeCRUD:
    "CRUD operations class for meme"

    @classmethod
    async def get_many(
        cls,
        async_session: async_sessionmaker[AsyncSession],
        skip: int = 0,
        limit: int = 100
        ) -> Sequence[Meme]:  # type: ignore
        "Coroutine for getting array of memes"
        async with async_session() as session:
            result = await session.execute(
                select(Meme).offset(skip).limit(limit)
            )

            return result.scalars().all()  # type: ignore

    @classmethod
    async def get_one(
        cls,
        meme_id: int,
        async_session: async_sessionmaker[AsyncSession]
        ) -> Meme | None:
        "Coroutine for getting a meme instance"
        async with async_session() as session:
            result = await session.execute(
                select(Meme).filter(Meme.id==meme_id)
            )
            return result.scalar_one_or_none()

    @classmethod
    async def create(
        cls,
        meme: MemeSchema,
        async_session: async_sessionmaker[AsyncSession]
    ) -> Meme:
        "Coroutine for creating a meme instance"
        async with async_session() as session:
            db_meme = Meme(**meme.dict())
            session.add(db_meme)
            try:
                await session.commit()
            except IntegrityError as error:
                raise HTTPException(
                    status_code=400,
                    detail="Meme with this name already exists"
                ) from error
            await session.refresh(db_meme)
            return db_meme


    @classmethod
    async def update(
        cls,
        meme: MemeSchema,
        async_session: async_sessionmaker[AsyncSession],
    ) -> Meme:
        "Couroutine for updating a meme instance"
        async with async_session() as session:
            meme_rows = await session.execute(
                select(Meme).filter(Meme.id==meme.id)
            )
            meme_row = meme_rows.scalar_one_or_none()

            if not meme_row:
                raise HTTPException(
                        status_code=404,
                        detail="Meme not found"
                    )

            meme_row.title = meme.title
            try:
                await session.commit()
            except IntegrityError as error:
                raise HTTPException(
                    status_code=400,
                    detail="Meme with this name already exists"
                ) from error
            await session.refresh(meme_row)
            return meme_row


    @classmethod
    async def delete(
        cls,
        meme_id: int,
        async_session: async_sessionmaker[AsyncSession]
    ) -> None:
        "Coroutine for deleting a meme instance"
        async with async_session() as session:
            meme = await cls.get_one(
                meme_id=meme_id,
                async_session=async_session
            )
            if meme:
                await session.delete(instance=meme)
            else:
                raise HTTPException(
                    status_code=404,
                    detail="Meme not found"
                )
            await session.commit()
