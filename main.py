"Main FastAPI module"

from fastapi import FastAPI

from services.memes import router as memes_router
from services.auth import router as auth_router

app = FastAPI(
    title="Memes API",
    description="Grant memes database",
    docs_url="/",
)

app.include_router(router=memes_router)
app.include_router(router=auth_router)
