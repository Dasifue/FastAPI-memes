"Async database connection module"

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from .settings import (
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
)


DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


engine = create_async_engine(
    url=DATABASE_URL,
    echo=True
)
session = async_sessionmaker(
    bind=engine,
    expire_on_commit=True
)

class Base(DeclarativeBase):
    "class for sqlalchemy ORM system"
