from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from .schema import BookSchema
from .service import book_service

router = APIRouter(
    prefix="/api/v1/book",
    tags=["Book API Endpoints"]
)

@router.post("", response_model=BookSchema)
def create_book(book: BookSchema, db: Session = Depends(get_db)):
    return book_service.create_book(db=db, book=book)

@router.get("/", response_model=list[BookSchema])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return book_service.get_books(db=db, skip=skip, limit=limit)

@router.get("/{book_id}", response_model=BookSchema)
def read_book(book_id: int, db: Session = Depends(get_db)):
    return book_service.get_book(db=db, book_id=book_id)

@router.put("/{book_id}", response_model=BookSchema)
def update_book(book_id: int, book: BookSchema, db: Session = Depends(get_db)):
    return book_service.update_book(db=db, book_id=book_id, book=book)

@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    return book_service.delete_book(db=db, book_id=book_id)
