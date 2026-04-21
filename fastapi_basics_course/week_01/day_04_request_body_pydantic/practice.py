"""
Практическое задание:
1. Используй Pydantic-модель как входной контракт.
2. Верни корректный `TicketOut` из route.
3. Убедись, что невалидный короткий title даёт validation error.

Например:
- request body: `{"title": "Checkout bug", "priority": "high", "description": "repro steps"}`
- response body: `{"id": 1, "title": "Checkout bug", "priority": "high", "description": "repro steps"}`
- request body с `{"title": "bad", ...}` -> `422`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field

app = FastAPI(title='Practice Day 4')


class TicketCreate(BaseModel):
    title: str = Field(min_length=5)
    priority: str
    description: str | None = None


class TicketOut(BaseModel):
    id: int
    title: str
    priority: str
    description: str | None = None


@app.post('/tickets', response_model=TicketOut)
def create_ticket(payload: TicketCreate) -> TicketOut:
    return TicketOut(id=1, title=payload.title, priority=payload.priority, description=payload.description)


client = TestClient(app)


def run_checks() -> None:
    response = client.post('/tickets', json={'title': 'Checkout bug', 'priority': 'high', 'description': 'repro steps'})
    assert response.status_code == 200, 'expected 200 OK response'
    assert response.json() == {
        'id': 1,
        'title': 'Checkout bug',
        'priority': 'high',
        'description': 'repro steps',
    }

    response = client.post('/tickets', json={'title': 'bad', 'priority': 'low'})
    assert response.status_code == 422, 'expected validation error 422'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
