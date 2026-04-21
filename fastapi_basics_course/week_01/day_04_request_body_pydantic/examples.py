from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title='FastAPI Basics Day 4')


class BookCreate(BaseModel):
    title: str = Field(min_length=3)
    author: str
    pages: int = Field(gt=0)


class BookOut(BaseModel):
    id: int
    title: str
    author: str
    pages: int


@app.post('/books', response_model=BookOut)
def create_book(payload: BookCreate) -> BookOut:
    return BookOut(id=1, **payload.model_dump())
