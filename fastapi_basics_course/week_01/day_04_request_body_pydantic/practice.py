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

from fastapi import FastAPI, status
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


@app.post('/tickets', response_model=TicketOut, status_code=status.HTTP_201_CREATED)
def create_ticket(payload: TicketCreate) -> TicketOut:
    # TODO: верни реальный TicketOut на основе payload, а не placeholder.
    return TicketOut(id=0, title='TODO', priority='TODO', description='TODO')


client = TestClient(app)


def run_checks() -> None:
    response = client.post('/tickets', json={'title': 'Checkout bug', 'priority': 'high', 'description': 'repro steps'})
    assert response.status_code == 201, 'expected 201 Created response'
    body = response.json()
    assert body['id'] > 0, 'created ticket should have positive id'
    assert body['title'] == 'Checkout bug', 'created ticket should echo request title'
    assert body['priority'] == 'high', 'created ticket should echo request priority'
    assert body['description'] == 'repro steps', 'created ticket should echo request description'

    response = client.post('/tickets', json={'title': 'bad', 'priority': 'low'})
    assert response.status_code == 422, 'expected validation error 422'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
