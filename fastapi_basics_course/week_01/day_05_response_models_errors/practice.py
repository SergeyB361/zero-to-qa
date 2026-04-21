"""
Практическое задание:
1. Верни корректный comment по id через `response_model`.
2. Для отсутствующего comment верни честный `404`.
3. Заполни осмысленный `detail` в error path.

Например:
- `GET /comments/1` -> `{"id": 1, "text": "first comment"}`
- `GET /comments/999` -> `404` и `{"detail": "comment not found"}`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

from fastapi import FastAPI, HTTPException, status
from fastapi.testclient import TestClient
from pydantic import BaseModel

app = FastAPI(title='Practice Day 5')
comments = {1: {'id': 1, 'text': 'first comment'}}


class CommentOut(BaseModel):
    id: int
    text: str


@app.get('/comments/{comment_id}', response_model=CommentOut)
def get_comment(comment_id: int) -> CommentOut:
    comment = comments.get(comment_id)
    if comment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='TODO')
    # TODO: верни реальный comment вместо placeholder.
    return CommentOut(id=0, text='TODO')


client = TestClient(app)


def run_checks() -> None:
    response = client.get('/comments/1')
    assert response.status_code == 200, 'expected 200 OK response'
    assert response.json() == {'id': 1, 'text': 'first comment'}, 'detail route should return exact comment payload'

    response = client.get('/comments/999')
    assert response.status_code == 404, 'expected 404 Not Found response'
    assert response.json()['detail'] == 'comment not found', 'not found branch should explain missing comment'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
