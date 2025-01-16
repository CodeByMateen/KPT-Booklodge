from fastapi import FastAPI
from src.database import engine, Base
from src.api.book.router import router as book_router

app = FastAPI(
    title="Bookly API",
    description="API for managing books",
    version="1.0"
)

# Include book routes
app.include_router(book_router)

@app.get("/")
def read_root():
    print("---------------------Hello World---------------------")
    return {"message": "Hello World"}

# Create the database tables
Base.metadata.create_all(bind=engine)