"Auth routers"
from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from .auth import auth_backend
from .manager import get_user_manager
from .models import User
from .schemas import UserRead, UserCreate

router = APIRouter(
    prefix="/memes",
    tags=["Memes"]
)


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/jwt",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="",
    tags=["auth"],
)
