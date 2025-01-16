from sqlalchemy.orm import Session
from fastapi import HTTPException
from .models import Book
from .schemas import BookSchema

class BookService:
    @staticmethod
    def create_book(db: Session, book: BookSchema):
        db_book = Book(
            title=book.title,
            author=book.author,
            publication_year=book.publication_year
        )
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book

    @staticmethod
    def get_books(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Book).offset(skip).limit(limit).all()

    @staticmethod
    def get_book(db: Session, book_id: int):
        book = db.query(Book).filter(Book.id == book_id).first()
        if book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        return book

    @staticmethod
    def update_book(db: Session, book_id: int, book: BookSchema):
        db_book = db.query(Book).filter(Book.id == book_id).first()
        if db_book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        
        for key, value in book.dict().items():
            setattr(db_book, key, value)
        
        db.commit()
        db.refresh(db_book)
        return db_book

    @staticmethod
    def delete_book(db: Session, book_id: int):
        db_book = db.query(Book).filter(Book.id == book_id).first()
        if db_book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        
        db.delete(db_book)
        db.commit()
        return {"message": "Book deleted successfully"}

book_service = BookService()