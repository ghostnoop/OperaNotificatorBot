from datetime import datetime

from pydantic import BaseModel


class Poster(BaseModel):
    id: str
    date: str
    title: str
    is_available: bool
    image: str
