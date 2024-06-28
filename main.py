"Main FastAPI module"

from fastapi import FastAPI

from services.memes import router as memes_router
from services.auth import router as auth_router


import os

print("DB_NAME:", os.getenv("DB_NAME"))
print("DB_USER:", os.getenv("DB_USER"))
print("DB_PASSWORD:", os.getenv("DB_PASSWORD"))
print("DB_HOST:", os.getenv("DB_HOST"))
print("DB_PORT:", os.getenv("DB_PORT"))
print("MINIO_HOST:", os.getenv("MINIO_HOST"))
print("MINIO_PORT:", os.getenv("MINIO_PORT"))
print("MINIO_ACCESS_KEY:", os.getenv("MINIO_ACCESS_KEY"))
print("MINIO_SECRET_KEY:", os.getenv("MINIO_SECRET_KEY"))


app = FastAPI(
    title="Memes API",
    description="Grant memes database",
    docs_url="/",
)

app.include_router(router=memes_router)
app.include_router(router=auth_router)
