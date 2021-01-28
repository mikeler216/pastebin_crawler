from datetime import datetime

from pydantic import BaseModel


class BaseSchema(BaseModel):
    class Config:
        orm_mode = True

    id: int


class PostSchemaBase(BaseModel):
    pastebin_id: str
    author: str
    post_text: str
    post_date: datetime


class PostSchema(BaseSchema, PostSchemaBase):
    pass
