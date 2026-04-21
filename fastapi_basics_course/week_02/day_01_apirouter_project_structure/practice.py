"""
Практическое задание:
1. Раздели endpoints по двум router-ам.
2. Сохрани корректные `prefix` и `tags`.
3. Проверь, что оба router-а подключены к приложению.

Например:
- `GET /accounts/` -> `[ {"id": 1, "login": "demo"} ]`
- `GET /reports/` -> `[ {"id": 1, "status": "ready"} ]`
- в `app.routes` должны быть оба пути: `/accounts/` и `/reports/`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

from fastapi import APIRouter, FastAPI
from fastapi.testclient import TestClient

app = FastAPI(title='Practice Week 2 Day 1')
accounts_router = APIRouter(prefix='/accounts', tags=['accounts'])
reports_router = APIRouter(prefix='/reports', tags=['reports'])


@accounts_router.get('/')
def list_accounts() -> list[dict[str, object]]:
    # TODO: верни осмысленный demo account.
    return [{'id': 0, 'login': 'TODO'}]


@reports_router.get('/')
def list_reports() -> list[dict[str, object]]:
    # TODO: верни осмысленный report status.
    return [{'id': 0, 'status': 'TODO'}]


app.include_router(accounts_router)
app.include_router(reports_router)
client = TestClient(app)


def run_checks() -> None:
    paths = {route.path for route in app.routes}
    assert '/accounts/' in paths, 'accounts router path is not registered'
    assert '/reports/' in paths, 'reports router path is not registered'

    response = client.get('/accounts/')
    assert response.status_code == 200, 'expected 200 OK response'
    assert response.json() == [{'id': 1, 'login': 'demo'}], 'accounts router response is incorrect'

    response = client.get('/reports/')
    assert response.status_code == 200, 'expected 200 OK response'
    assert response.json() == [{'id': 1, 'status': 'ready'}], 'reports router response is incorrect'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
