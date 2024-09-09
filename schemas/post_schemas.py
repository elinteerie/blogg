from pydantic import BaseModel
from datetime import datetime


class PostBase(BaseModel):
    title: str
    content: str
    creator: str
    image_url: str

class PostDisplay(BaseModel):
    id: int
    title: str
    content: str
    creator: str
    timestamp: datetime
    image_url: str

    class Config():
        orm_mode = True