"User model"
from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession

from services.database import Base, session as assync_session

class User(SQLAlchemyBaseUserTable[int], Base):
    "User model"
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(default=False, nullable=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    "async session"
    async with assync_session() as session:
        yield session

async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    "yields user"
    yield SQLAlchemyUserDatabase(session, User)
