"Main FastAPI module"

from fastapi import FastAPI

from services.memes import router

app = FastAPI(
    title="Memes API",
    description="Grant memes database",
    docs_url="/",
)

app.include_router(router=router)
