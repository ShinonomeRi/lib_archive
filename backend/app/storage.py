from typing import List, Optional
from .models import Book, BookCreate

# "База данных" в памяти
_books_db: List[Book] = []


def init_demo_data() -> None:
    """Заполняем демо-данными при старте приложения."""
    global _books_db
    if _books_db:
        return  # уже инициализировано

    demo_books = [
        Book(id=1, title="Война и мир", author="Лев Толстой", year=1869,
             tags=["роман", "классика"]),
        Book(id=2, title="Преступление и наказание", author="Фёдор Достоевский", year=1866,
             tags=["роман", "психология"]),
        Book(id=3, title="Гарри Поттер и философский камень", author="Дж. Роулинг", year=1997,
             tags=["фэнтези", "подростковая литература"]),
    ]
    _books_db = demo_books


def list_books() -> List[Book]:
    return list(_books_db)


def get_book(book_id: int) -> Optional[Book]:
    for book in _books_db:
        if book.id == book_id:
            return book
    return None


def create_book(data: BookCreate) -> Book:
    if _books_db:
        new_id = max(book.id for book in _books_db) + 1
    else:
        new_id = 1

    book = Book(id=new_id, **data.dict())
    _books_db.append(book)
    return book


def search_books(query: str) -> List[Book]:
    q = query.lower()
    result = []
    for book in _books_db:
        if (
            q in book.title.lower()
            or q in book.author.lower()
            or any(q in tag.lower() for tag in book.tags)
        ):
            result.append(book)
    return result
