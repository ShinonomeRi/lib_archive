from pydantic import BaseModel
from typing import Optional, List


class BookBase(BaseModel):
    title: str
    author: str
    year: int
    tags: List[str] = []


class BookCreate(BookBase):
    """Модель для создания книги (без id)."""
    pass


class Book(BookBase):
    """Модель книги, которая возвращается наружу (с id)."""
    id: int
