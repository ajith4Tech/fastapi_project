# 🚀 FastAPI Learning Projects

This repository contains beginner-friendly learning projects to explore **FastAPI** and modern API development with Python.

---

## 🔧 Environment Setup
# Create virtual environment
python3 -m venv fastapivenv

# Activate on Unix/Mac
source fastapivenv/bin/activate

### ✅ What is FastAPI?
FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.

### 💡 Architecture
Webpage → FastAPI server → API response

### ⚙️ Python Virtual Environment
Isolated environment to manage project-specific dependencies.

```bash


# Install FastAPI and Uvicorn
pip install fastapi
pip install "uvicorn[standard]"



🌐 ASGI vs WSGI
| Interface | Type         | Framework | Request Handling          |
| --------- | ------------ | --------- | ------------------------- |
| **WSGI**  | Synchronous  | Gunicorn  | Sequential                |
| **ASGI**  | Asynchronous | Uvicorn   | Concurrent, more scalable |


🧪 Running the FastAPI App

# Run with Uvicorn (for development)
uvicorn basic_version:app --reload

# (For newer versions)
fastapi run basic_version.py

🧱 Core Concepts with Examples
1. ✅ Basic API Setup

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Project!"}

2. 📌 CRUD Operations (Books)
📖 GET - Read All Books

@app.get("/books")
async def read_all_books():
    return BOOKS

➕ POST - Add a Book

from fastapi import Body

@app.post("/books/add-book")
async def add_book(new_book = Body()):
    BOOKS.append(new_book)
    return {"message": "Book added successfully"}

📝 PUT - Update Book

@app.put("/books/update-book/{book_title}")
async def update_book(book_title: str, updated_book = Body()):
    ...

❌ DELETE - Delete Book

@app.delete("/books/delete-book/{book_title}")
async def delete_book(book_title: str):
    ...

3. 🛣️ Path Parameters

Used to identify resources dynamically via URL.

@app.get("/books/book-title/{book_title}")
async def read_book(book_title: str):
    ...

✅ Note: Order matters in path parameters.
4. 🔎 Query Parameters

Used for filtering/sorting data via URL queries.

@app.get("/books/")
async def read_by_query(category: Optional[str] = None):


5. 🧠 Case-Insensitive Matching

book.get('title').casefold() == book_title.casefold()

Use .casefold() for Unicode-aware, case-insensitive comparisons (e.g., "straße".casefold() vs "strasse").
6. 🧾 Request Body with Pydantic

from pydantic import BaseModel, Field

class BookRequest(BaseModel):
    book_title: str = Field(min_length=3)
    rating: int = Field(gt=1, le=5)

Use .model_dump() in Pydantic v2 to extract data.
7. 🚦 HTTP Status Codes & Exceptions

from fastapi import status, HTTPException

@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int):
    raise HTTPException(status_code=404, detail="Book not found")


8. ✅ Validation for Path & Query

from fastapi import Path, Query

@app.get("/books/{book_id}")
async def get_book(book_id: int = Path(gt=0)):
    ...

@app.get("/books/")
async def get_books(book_rating: Optional[int] = Query(gt=0, lt=6)):
    ...

9. 🧠 Dynamic Book ID Generation

def find_book_id(book: Book):
    book.book_id = 1 if len(BOOKS) == 0 else BOOKS[-1].book_id + 1
    return book

📁 File Overview
File Name	Concepts Covered
basic_version.py	CRUD, Path & Query Params, Request Body basics
project_2.py	Pydantic, Field validation, Status codes, Exception handling, ID generation