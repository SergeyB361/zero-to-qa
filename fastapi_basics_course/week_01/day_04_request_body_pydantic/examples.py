from fastapi import FastAPI, status
from fastapi.testclient import TestClient
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


@app.post('/books', response_model=BookOut, status_code=status.HTTP_201_CREATED)
def create_book(payload: BookCreate) -> BookOut:
    return BookOut(id=1, **payload.model_dump())


if __name__ == '__main__':
    client = TestClient(app)
    response = client.post('/books', json={'title': 'Domain Testing', 'author': 'Anna', 'pages': 240})
    print('POST /books ->', response.status_code, response.json())
