"Authenticated strategy with JWT in cookie"
import os

from fastapi_users.authentication import AuthenticationBackend, JWTStrategy, CookieTransport
from dotenv import load_dotenv

load_dotenv()

cookie_transport = CookieTransport(cookie_name="memesauth", cookie_max_age=3600)


SECRET = os.getenv("JWT_SECRET_KEY")

def get_jwt_strategy() -> JWTStrategy:
    "auth staregy"
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
