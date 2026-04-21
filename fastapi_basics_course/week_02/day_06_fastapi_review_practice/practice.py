"""
Практическое задание:
1. Собери маленький ticket API из уже изученных блоков.
2. Сохрани dependency, list/detail routes и create route.
3. Для отсутствующего ticket верни `404`.

Например:
- `GET /tickets` -> `{"actor": "anonymous", "limit": 10, "items": [...]}`
- `GET /tickets/1` -> `{"id": 1, "title": "Bug in checkout", "status": "open"}`
- `POST /tickets` c `{"title": "Auth issue"}` -> `201` и новый ticket
- `GET /tickets/999` -> `404`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

from typing import Annotated

from fastapi import Depends, FastAPI, Header, HTTPException, Query, status
from fastapi.testclient import TestClient
from pydantic import BaseModel

app = FastAPI(title='Practice Week 2 Day 6')
tickets = [{'id': 1, 'title': 'Bug in checkout', 'status': 'open'}]


class TicketCreate(BaseModel):
    title: str


def get_actor(x_actor: Annotated[str | None, Header()] = None) -> str:
    return x_actor or 'anonymous'


@app.get('/tickets')
def list_tickets(actor: Annotated[str, Depends(get_actor)], limit: int = Query(10, ge=1, le=50)) -> dict[str, object]:
    return {'actor': actor, 'limit': limit, 'items': tickets[:limit]}


@app.get('/tickets/{ticket_id}')
def get_ticket(ticket_id: int) -> dict[str, object]:
    for ticket in tickets:
        if ticket['id'] == ticket_id:
            return ticket
    raise HTTPException(status_code=404, detail='ticket not found')


@app.post('/tickets', status_code=status.HTTP_201_CREATED)
def create_ticket(payload: TicketCreate) -> dict[str, object]:
    item = {'id': len(tickets) + 1, 'title': payload.title, 'status': 'open'}
    tickets.append(item)
    return item


client = TestClient(app)


def run_checks() -> None:
    response = client.get('/tickets')
    assert response.status_code == 200, 'expected 200 OK response'
    assert response.json()['actor'] == 'anonymous', 'default actor dependency result is incorrect'

    response = client.get('/tickets/1')
    assert response.status_code == 200, 'expected 200 OK response'
    assert response.json()['title'] == 'Bug in checkout', 'detail route should return seeded ticket'

    response = client.get('/tickets/999')
    assert response.status_code == 404, 'expected 404 Not Found response'

    response = client.post('/tickets', json={'title': 'Auth issue'})
    assert response.status_code == 201, 'expected 201 Created response'
    assert response.json()['title'] == 'Auth issue', 'POST /tickets should create Auth issue ticket'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
