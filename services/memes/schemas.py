"Pydantic schemas"

from datetime import datetime

from pydantic import BaseModel

class MemeBaseSchema(BaseModel):
    "Base meme schema"
    title: str

class MemeCreationSchema(MemeBaseSchema):
    "Schema to create and update meme"
    file: str

class MemeSchema(MemeBaseSchema):
    "Schema for swagger response model"
    id: int
    file: str
    uploaded_at: datetime
