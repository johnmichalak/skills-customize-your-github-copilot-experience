# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API for managing a collection of books with the FastAPI framework. Practice defining data models, creating HTTP endpoints, validating request data, and returning appropriate status codes.

## 📝 Tasks

### 🛠️ Define the Book Models

#### Description
Complete the Pydantic models in `starter-code.py`. Pydantic models describe and validate the data accepted and returned by the API.

#### Requirements
Completed program should:

- Define a `BookCreate` model with `title`, `author`, and `year` fields.
- Require `title` and `author` to be strings and `year` to be an integer.
- Define a `Book` response model that includes an integer `id` in addition to the fields from `BookCreate`.

### 🛠️ Create the API Endpoints

#### Description
Implement endpoints that let clients create, list, retrieve, and delete books in the provided in-memory collection.

#### Requirements
Completed program should:

- Implement `POST /books` to add a book and return it with status code `201`.
- Implement `GET /books` to return all books.
- Implement `GET /books/{book_id}` to return the book with the requested ID.
- Implement `DELETE /books/{book_id}` to remove a book and return status code `204`.
- Assign each new book a unique integer ID.

### 🛠️ Validate Requests and Handle Errors

#### Description
Improve the API by constraining input values and returning clear HTTP errors when a requested resource does not exist.

#### Requirements
Completed program should:

- Reject an empty `title` or `author` through Pydantic field validation.
- Accept publication years from `1450` through the current year.
- Return status code `404` with a clear message when a requested book ID does not exist.
- Run locally with `fastapi dev starter-code.py` and expose interactive documentation at `http://127.0.0.1:8000/docs`.
