"Main FastAPI module"

from fastapi import FastAPI
from fastapi.testclient import TestClient

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


client = TestClient(app)

def test_read_main():
    "testing home page"
    response = client.get("/")
    assert response.status_code == 200


def test_register():
    "testing registration"
    response = client.post("/auth/register/", json={
        "email": "test@testing.com",
        "password": "test123"
    })
    assert response.status_code == 201