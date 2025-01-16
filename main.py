from fastapi import FastAPI
from src.database import engine, Base
from src.api.book.router import router as book_router

app = FastAPI(
    title="Bookly API",
    description="API for managing books",
    version="1.0"
)

@app.get("/")
def read_root():
    print("---------------------Hello World---------------------")
    return {"message": "Hello World"}

# Include book routes
app.include_router(book_router)

# Create the database tables
Base.metadata.create_all(bind=engine)