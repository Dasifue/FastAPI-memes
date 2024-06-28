"Routers to get images"

from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import Response
from minio.error import S3Error

from services.minio_storage import client
from services.auth import fastapi_users, User

router = APIRouter(
    prefix="/media",
    tags=["Media"]
)

authenticated_user = fastapi_users.current_user()

@router.get("/{file_name}")
async def get_image(file_name: str, user: User = Depends(authenticated_user)):
    "Endpoint returns image"
    try:
        response = client.get_object(
            bucket_name="memes",
            object_name=file_name,
        )
    except S3Error as error:
        raise HTTPException(
            status_code=404,
            detail="Media not found"
        ) from error

    return Response(content=response.read(), status_code=200, media_type="image/png")
