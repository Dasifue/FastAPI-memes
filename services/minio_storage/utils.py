"Minio storage utils"

from fastapi import HTTPException, File
from minio.error import S3Error

from .storage import client

def upload_file(file: File) -> None:
    "Function uploads file"
    try:
        client.put_object(
            bucket_name="memes",
            object_name=file.filename,
            data=file.file,
            length=file.size,
            content_type=file.content_type
        )
    except S3Error as error:
        raise HTTPException(status_code=400, detail=str(error)) from error


def delete_file(file_name: str) -> None:
    "Function deletes file"
    try:
        client.remove_object(
            bucket_name="memes",
            object_name=file_name,
        )
    except S3Error as error:
        raise HTTPException(status_code=400, detail=str(error)) from error
