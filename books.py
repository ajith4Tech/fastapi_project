
from fastapi import FastAPI

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
    {'title': 'five', 'author': 'testfive', 'year': 2026, 'category': 'testcategory' }
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

@app.get("/books/")         #returns all the books by category. here category is the query parameter.
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
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