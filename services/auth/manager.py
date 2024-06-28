"User manager"
import os
from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin
from dotenv import load_dotenv

from .models import User, get_user_db

load_dotenv()

SECRET = os.getenv("USER_MANAGER_SECRET_KEY")


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    "Class for managing user model"
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")



async def get_user_manager(user_db=Depends(get_user_db)):
    "Yields user manager"
    yield UserManager(user_db)
