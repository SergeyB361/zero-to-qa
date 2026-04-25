"""
Практическое задание:
1. Оставь HTTP-логику в router.
2. Пусть создание issue идёт через service layer.
3. Храни in-memory storage внутри repository.

Например:
- первый `GET /issues` -> `[{'id': 1, 'title': 'Seed issue'}]`
- `POST /issues` c `{"title": "Login bug"}` -> `201` и `{'id': 2, 'title': 'Login bug'}`
- повторный `GET /issues` -> уже 2 записи

Критерий готовности: `run_checks()` проходит без ошибок.
"""

from fastapi import APIRouter, FastAPI, status
from fastapi.testclient import TestClient
from pydantic import BaseModel


class IssueCreate(BaseModel):
    title: str


class IssueRepository:
    def __init__(self) -> None:
        self._items = [{'id': 1, 'title': 'Seed issue'}]

    def list_all(self) -> list[dict[str, object]]:
        return list(self._items)

    def create(self, title: str) -> dict[str, object]:
        item = {'id': len(self._items) + 1, 'title': title}
        self._items.append(item)
        return item


class IssueService:
    def __init__(self, repo: IssueRepository) -> None:
        self.repo = repo

    def list_issues(self) -> list[dict[str, object]]:
        return self.repo.list_all()

    def create_issue(self, title: str) -> dict[str, object]:
        # TODO: создать issue через repository и вернуть item.
        return {'id': 0, 'title': 'TODO'}


def build_app() -> FastAPI:
    repo = IssueRepository()
    service = IssueService(repo)
    router = APIRouter(prefix='/issues', tags=['issues'])

    @router.get('')
    def list_issues() -> list[dict[str, object]]:
        return service.list_issues()

    @router.post('', status_code=status.HTTP_201_CREATED)
    def create_issue(payload: IssueCreate) -> dict[str, object]:
        return service.create_issue(payload.title)

    app = FastAPI(title='Practice Project Layout')
    app.include_router(router)
    return app


def run_checks() -> None:
    client = TestClient(build_app())

    response = client.get('/issues')
    assert response.status_code == 200, 'expected 200 OK for issues list'
    assert response.json() == [{'id': 1, 'title': 'Seed issue'}], 'seed issue should be present before create'

    response = client.post('/issues', json={'title': 'Login bug'})
    assert response.status_code == 201, 'expected 201 Created for POST /issues'
    assert response.json() == {'id': 2, 'title': 'Login bug'}, 'service should create issue via repository'

    response = client.get('/issues')
    assert len(response.json()) == 2, 'after create there should be two issues in storage'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
