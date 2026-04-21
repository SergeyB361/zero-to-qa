"""
Практическое задание:
1. Доделай dependency для чтения actor из header.
2. Сохрани валидацию `limit` и `offset` через `Query`.
3. Верни итоговый response с actor, limit и offset.

Например:
- без header -> `{"actor": "system", "limit": 20, "offset": 0}`
- с `x-actor: qa-user` и `?limit=5&offset=3` -> `{"actor": "qa-user", "limit": 5, "offset": 3}`
- `limit=999` -> `422`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

from typing import Annotated

from fastapi import Depends, FastAPI, Header, Query
from fastapi.testclient import TestClient

app = FastAPI(title='Practice Day 6')


def get_actor(x_actor: Annotated[str | None, Header()] = None) -> str:
    return x_actor or 'system'


@app.get('/audit/events')
def list_events(actor: Annotated[str, Depends(get_actor)], limit: int = Query(default=20, ge=1, le=50), offset: int = Query(default=0, ge=0)) -> dict[str, object]:
    return {'actor': actor, 'limit': limit, 'offset': offset}


client = TestClient(app)


def run_checks() -> None:
    response = client.get('/audit/events')
    assert response.status_code == 200, 'expected 200 OK response'
    assert response.json() == {'actor': 'system', 'limit': 20, 'offset': 0}, 'defaults/dependency result are incorrect'

    response = client.get('/audit/events?limit=5&offset=3', headers={'x-actor': 'qa-user'})
    assert response.status_code == 200, 'expected 200 OK response'
    assert response.json() == {'actor': 'qa-user', 'limit': 5, 'offset': 3}, 'custom header/query values are not reflected correctly'

    response = client.get('/audit/events?limit=999')
    assert response.status_code == 422, 'expected validation error 422'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
