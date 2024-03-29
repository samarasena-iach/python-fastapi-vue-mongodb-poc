from fastapi import APIRouter, HTTPException, Body
from typing import List, Union
from app.models.book import Book
from pymongo import MongoClient
from bson import ObjectId

router = APIRouter()

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["bookstore"]
collection = db["books"]

@router.get("/books/test")
def read_root():
    return {"message": "Welcome to Book Store!"}

@router.get("/books/", response_model=List[Book])
async def get_books():
    books = []
    for book_data in collection.find():
        books.append(Book(**book_data))
    return books

@router.get("/books/{book_id}", response_model=Book)
def read_book(book_id: str):
    book = collection.find_one({"_id": ObjectId(book_id)})
    if book:
        return book
    else:
        raise HTTPException(status_code=404, detail="Book not found")

@router.post("/books/", response_model=Union[List[Book], Book])
async def create_books(books: Union[List[Book], Book] = Body(...)):
    if isinstance(books, list):  # If the payload is a list of books
        created_books = []
        for book in books:
            book_dict = book.dict()
            inserted_book = collection.insert_one(book_dict)
            book_dict["_id"] = str(inserted_book.inserted_id)
            created_books.append(book_dict)
        return created_books
    else:  # If the payload is a single book
        book_dict = books.dict()
        inserted_book = collection.insert_one(book_dict)
        book_dict["_id"] = str(inserted_book.inserted_id)
        return book_dict

@router.put("/books/{book_id}", response_model=Book)
def update_book(book_id: str, book: Book):
    existing_book = collection.find_one({"_id": ObjectId(book_id)})
    if existing_book:
        updated_book = collection.update_one({"_id": ObjectId(book_id)}, {"$set": book.dict()})
        if updated_book.modified_count == 1:
            return book
        else:
            raise HTTPException(status_code=500, detail="Internal server error")
    else:
        raise HTTPException(status_code=404, detail="Book not found")

@router.delete("/books/{book_id}")
def delete_book(book_id: str):
    deleted_book = collection.delete_one({"_id": ObjectId(book_id)})
    if deleted_book.deleted_count == 1:
        return {"message": "Book deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Book not found")