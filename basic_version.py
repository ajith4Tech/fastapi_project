from typing import Optional
from fastapi import FastAPI, Body


app = FastAPI()

'''
This is the first API endpoint written just to test the FastAPI setup.


@app.get("/api-endpoint")               #@app.get is a decorator that tells FastAPI that this function is an API endpoint with get method.
async def first_api():                  #async stands for asynchronous. for FastAPI we dont need to explicitly use async because it is already asynchronous.
    return {
        "message" : "Hello Ajith"
    }

'''



#list of books
BOOKS = [
    {'title': 'one', 'author': 'testone', 'year': 2022, 'category': 'testcategory' },
    {'title': 'two', 'author': 'testtwo', 'year': 2023, 'category': 'testcategory2' },
    {'title': 'three', 'author': 'testthree', 'year': 2024, 'category': 'testcategory' },
    {'title': 'four', 'author': 'testfour', 'year': 2025, 'category': 'testcategory2' },
    {'title': 'five', 'author': 'testfive', 'year': 2026, 'category': 'testcategory' },
    {'title': 'six', 'author': 'testone', 'year': 2022, 'category': 'testcategory' },
    {'title': 'seven', 'author': 'testtwo', 'year': 2023, 'category': 'testcategory2' },
    {'title': 'eight', 'author': 'testthree', 'year': 2024, 'category': 'testcategory' },
    {'title': 'nine', 'author': 'testone', 'year': 2025, 'category': 'testcategory2' },
    {'title': 'ten', 'author': 'testfive', 'year': 2026, 'category': 'testcategory' }
]

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Project!"}

@app.get("/books")              #returns all the books 
async def read_all_books():
    return BOOKS

@app.get("/books/book-title/{book_title}")          # Added book-title to path to avoid order mismatch. returns a specific book by title. here title is the path parameter.
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
    return {"error": "Book not found", "statuscode": 404}

@app.get("/books/")         #returns all the books by category. here category is the query parameter. Optional is used and the default value is None is set because any query parameter can be passed or not.
async def read_category_by_query(category: Optional[str] = None, author: Optional[str] = None):
    books_to_return = []
    for book in BOOKS:
        if category and book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
        elif author and  book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    if books_to_return:
        return books_to_return
    return {"error": "No books found in this category", "statuscode": 404}

@app.get("/books/book-author/{author}")    # Added book-author to avoid order mismatch. returns all the books by author name. here book_author is the path parameter and category is the query parameter.
async def read_catgory_by_author(author: str, category: str):
    books_to_return = []
    print("Author:", author, "Category:", category)
    for book in BOOKS:
        print(book.get('author').casefold(), book.get('category').casefold(), author.casefold(), category.casefold())
        if book.get('author').casefold() == author.casefold() and book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    
    if books_to_return:
        return books_to_return
    return {"error": f"No books found by this {author} in this {category}", "statuscode": 404}

@app.post("/books/add-book")  # Adds a new book to the list. Here we are using post method to add a new book. Body is used to get the data from the request body.
async def add_book(new_book = Body()):
    if not new_book or not isinstance(new_book, dict):
        return {"error": "Invalid book data", "statuscode": 400}
    BOOKS.append(new_book)
    return {"message": "Book added successfully", "statuscode": 201, "book": new_book}


@app.put("/books/update-book/{book_title}")  # Updates an existing book by title. Here we are using put method to update an existing book.
async def update_book(book_title: str, updated_book = Body()):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            book.update(updated_book)
            return {"message": "Book updated successfully", "statuscode": 200, "book": book}
    return {"error": "Book not found", "statuscode": 404}


@app.delete("/books/delete-book/{book_title}")  # Deletes a book by title. Here we are using delete method to delete a book.
async def delete_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            BOOKS.remove(book)
            return {"message": "Book deleted successfully", "statuscode": 200}
    return {"error": "Book not found", "statuscode": 404}