from datetime import datetime

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field

app = FastAPI(title="Book API")


class BookCreate(BaseModel):
    # TODO: Define title, author, and year with the required validation.
    pass


class Book(BookCreate):
    # TODO: Add the book ID.
    pass


books: list[Book] = []
next_book_id = 1
current_year = datetime.now().year


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate) -> Book:
    # TODO: Assign a unique ID, save the book, and return it.
    raise NotImplementedError


@app.get("/books", response_model=list[Book])
def list_books() -> list[Book]:
    # TODO: Return all books.
    raise NotImplementedError


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    # TODO: Return the matching book or raise HTTPException with status 404.
    raise NotImplementedError


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int) -> Response:
    # TODO: Delete the matching book or raise HTTPException with status 404.
    raise NotImplementedError
