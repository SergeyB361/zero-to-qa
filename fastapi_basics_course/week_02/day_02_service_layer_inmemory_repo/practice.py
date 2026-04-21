"""
Практическое задание:
1. Оставь route тонким и использующим service layer.
2. Держи in-memory storage внутри repository.
3. Проверь, что создание аккаунта реально меняет storage.

Например:
- первый `GET /accounts` -> `[ {"id": 1, "login": "admin"} ]`
- `POST /accounts` c `{"login": "qa-user"}` -> `{"id": 2, "login": "qa-user"}`
- повторный `GET /accounts` -> уже 2 записи

Критерий готовности: `run_checks()` проходит без ошибок.
"""

from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel

app = FastAPI(title='Practice Week 2 Day 2')


class AccountCreate(BaseModel):
    login: str


class AccountRepository:
    def __init__(self) -> None:
        self._items = [{'id': 1, 'login': 'admin'}]

    def list_all(self) -> list[dict[str, object]]:
        return list(self._items)

    def create(self, payload: dict[str, object]) -> dict[str, object]:
        item = {'id': len(self._items) + 1, **payload}
        self._items.append(item)
        return item


class AccountService:
    def __init__(self, repo: AccountRepository) -> None:
        self.repo = repo

    def list_accounts(self) -> list[dict[str, object]]:
        return self.repo.list_all()

    def create_account(self, login: str) -> dict[str, object]:
        return self.repo.create({'login': login})


repo = AccountRepository()
service = AccountService(repo)


@app.get('/accounts')
def list_accounts() -> list[dict[str, object]]:
    return service.list_accounts()


@app.post('/accounts')
def create_account(payload: AccountCreate) -> dict[str, object]:
    return service.create_account(payload.login)


client = TestClient(app)


def run_checks() -> None:
    response = client.get('/accounts')
    assert response.status_code == 200, 'expected 200 OK response'
    assert response.json() == [{'id': 1, 'login': 'admin'}], 'list route should return seeded admin account'

    response = client.post('/accounts', json={'login': 'qa-user'})
    assert response.status_code == 200, 'expected 200 OK response'
    assert response.json()['login'] == 'qa-user', 'POST /accounts should create qa-user account'

    response = client.get('/accounts')
    assert len(response.json()) == 2, 'after creation there should be two accounts'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
