from fastapi import FastAPI, HTTPException
from typing import List, Optional

from .models import Book, BookCreate
from . import storage

app = FastAPI(
    title="Electronic Library Service",
    description="Сервис для управления электронной библиотекой и архивом (демо-версия).",
    version="0.1.0",
)


@app.on_event("startup")
async def startup_event():
    """Инициализация демо-данных при запуске приложения."""
    storage.init_demo_data()


@app.get("/books", response_model=List[Book])
async def list_books(q: Optional[str] = None):
    """
    Получить список книг.
    - без параметров: все книги;
    - с q=...: поиск по названию, автору и тегам.
    """
    if q:
        return storage.search_books(q)
    return storage.list_books()


@app.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: int):
    """Получить одну книгу по её идентификатору."""
    book = storage.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book


@app.post("/books", response_model=Book, status_code=201)
async def create_book(book_data: BookCreate):
    """
    Добавить новую книгу.

    Пример JSON:
    {
      "title": "Новая книга",
      "author": "Автор",
      "year": 2024,
      "tags": ["наука", "учебник"]
    }
    """
    return storage.create_book(book_data)
