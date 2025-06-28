from fastapi import FastAPI, Path, Query, HTTPException
from typing import Optional
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()
class Book:
    book_id: int
    book_title: str
    book_author: str
    book_year: int
    description: str
    rating: int 
    
    def __init__(self, book_id: int, book_title: str, book_author: str, book_year: int, description: str, rating: int):
        self.book_id = book_id
        self.book_title = book_title
        self.book_author = book_author
        self.book_year = book_year
        self.description = description
        self.rating = rating

class BookRequest(BaseModel): # BaseModel is used to validate the data coming from the request body. it is taken from pydantic library.
    book_id: Optional[int] = Field(description="Id is not required", default=None)  # book_id is optional and will be assigned automatically when a new book is created.
    book_title: str = Field(min_length = 3)
    book_author: str = Field(min_length = 1)
    book_year: int = Field(description="The year the book was published", gt=1900, le=2100)  # year should be between 1901 and 2100, inclusive. gt means greater than and le means less than or equal to.
    description: str = Field(min_length = 5, max_length=150)
    rating: int = Field(gt=1, le=5)  # rating should be between 1 and 5, inclusive. gt means greater than and le means less than or equal to.
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "book_title" : "New Book Title",
                "book_author": "New Author",
                "book_year": 2023,
                "description": "A brief description of the book.",
                "rating": 4
            }
        }
    }

BOOKS = [
    Book(1, "Computer Organisation", "Ajith", 2022, "A book on computer organisation", 5),
    Book(2, "Data Structures", "James", 2024, "A book on data structures", 4),
    Book(3, "Algorithms", "Alice", 2024, "A book on algorithms", 5),
    Book(4, "Operating Systems", "Bob", 2025, "A book on operating systems", 4),
    Book(5, "Database Systems", "Charlie", 2026, "A book on database systems", 5),
    Book(6, "Computer Networks", "David", 2022, "A book on computer networks", 4),
    Book(7, "Software Engineering", "Ajith", 2023, "A book on software engineering", 5),
]


@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    """
    Returns all the books.
    """
    return BOOKS

@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    """
    Returns a specific book by its ID.
    """
    for book in BOOKS:
        if book.book_id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.get("/books/" ,status_code=status.HTTP_200_OK)
async def read_books_by_rating_or_year(
    book_rating: Optional[int] = Query(gt=0, lt=6, default=None),
    year: Optional[int] = Query(gt=1900, le=2100, default=None)
    ):
    """
    Returns all the books with a specific rating.
    """
    books_to_return = []
    for book in BOOKS:
        if book_rating and book.rating == book_rating:
            books_to_return.append(book)
        elif year and book.book_year == year:
            books_to_return.append(book)
    
    if books_to_return:
        return books_to_return
    return {"error": "No books found with this rating", "statuscode": 404}

@app.post("/create_book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request:BookRequest):
    '''
    Unpack the BookRequest model to create a new Book instance. 
    ** will unpack the dictionary into keyword arguments. 
    dict() is depricated in pydantic v2, so we use model_dump() instead.
    '''
    new_book = Book(**book_request.model_dump())
      
    BOOKS.append(find_book_id(new_book))
    return {"message": "Book created successfully", "book": new_book}

@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].book_id == book.book_id:
            BOOKS[i] = book
            book_changed = True
            return {"message": "Book updated successfully", "book": book}
    if not book_changed:
            raise HTTPException(status_code=404, detail="Book not found for update")
            
@app.delete("/books/delete_book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int= Path(gt=0)):
    book_deleted = False
    for i in range(len(BOOKS)):
        if BOOKS[i].book_id == book_id:
            del BOOKS[i]
            book_deleted = True
            return {"message": "Book deleted successfully"}
    if not book_deleted:
        raise HTTPException(status_code=404, detail="Book not found for deletion")

def find_book_id(book : Book):
    book.book_id = 1 if len(BOOKS) == 0 else BOOKS[-1].book_id + 1
    return book