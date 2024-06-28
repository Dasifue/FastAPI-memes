"User schemas"
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    "Read user shcema"


class UserCreate(schemas.BaseUserCreate):
    "Create user schema"
