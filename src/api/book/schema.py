from pydantic import BaseModel 

class BookSchema(BaseModel):
    title: str
    author: str
    publication_year: int

    class Config:
        from_attributes = True
