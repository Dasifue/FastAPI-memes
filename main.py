"Main FastAPI module"

from fastapi import FastAPI

app = FastAPI(
    title="Memes API",
    description="Grant memes database",
    docs_url="/",
)
