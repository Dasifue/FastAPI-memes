"Main FastAPI module"

from fastapi import FastAPI

from services.memes import router as memes_router
from services.auth import router as auth_router
from services.media import router as media_router


app = FastAPI(
    title="Memes API",
    description="Grant memes database",
    docs_url="/",
)

app.include_router(router=memes_router)
app.include_router(router=auth_router)
app.include_router(router=media_router)
