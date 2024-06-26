"Minio utils"

from minio import Minio

from .settings import (
    MINIO_HOSTNAME,
    MINIO_PORT,
    MINIO_ACCESS_KEY,
    MINIO_SECRET_KEY
)

client = Minio(
    f"{MINIO_HOSTNAME}:{MINIO_PORT}",
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False,
)
