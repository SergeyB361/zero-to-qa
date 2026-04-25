"""
Мини-проект недели 1:
собери service skeleton для домена users + tasks.

Что нужно сделать:
1. реализовать create/list для users;
2. реализовать create/list/get для tasks;
3. вернуть согласованный 404 error contract для missing task;
4. оставить route, service и repository разделёнными.

Например:
- `POST /api/v1/users` -> `201`, `{"id": 1, "name": "Anna"}`
- `POST /api/v1/tasks` -> `201`, `{"id": 1, "title": "Prepare demo", "owner_id": 1}`
- `GET /api/v1/tasks/1` -> `200`, задача
- `GET /api/v1/tasks/999` -> `404`, `{"detail": "task not found", "code": "task_not_found"}`
"""

from dataclasses import dataclass

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
from fastapi.testclient import TestClient
from pydantic import BaseModel


@dataclass(slots=True)
class AppSettings:
    app_name: str = 'Service Skeleton'
    api_prefix: str = '/api/v1'


class UserCreate(BaseModel):
    name: str


class TaskCreate(BaseModel):
    title: str
    owner_id: int


class UserRepository:
    def __init__(self) -> None:
        self._items: list[dict[str, object]] = []

    def list_all(self) -> list[dict[str, object]]:
        return list(self._items)

    def create(self, name: str) -> dict[str, object]:
        item = {'id': len(self._items) + 1, 'name': name}
        self._items.append(item)
        return item


class TaskRepository:
    def __init__(self) -> None:
        self._items: list[dict[str, object]] = []

    def list_all(self) -> list[dict[str, object]]:
        return list(self._items)

    def get_by_id(self, task_id: int) -> dict[str, object] | None:
        return next((item for item in self._items if item['id'] == task_id), None)

    def create(self, title: str, owner_id: int) -> dict[str, object]:
        item = {'id': len(self._items) + 1, 'title': title, 'owner_id': owner_id}
        self._items.append(item)
        return item


class UserService:
    def __init__(self, repo: UserRepository) -> None:
        self.repo = repo

    def list_users(self) -> list[dict[str, object]]:
        return self.repo.list_all()

    def create_user(self, name: str) -> dict[str, object]:
        # TODO: создать пользователя через UserRepository.
        return {'id': 0, 'name': 'TODO'}


class TaskService:
    def __init__(self, repo: TaskRepository) -> None:
        self.repo = repo

    def list_tasks(self) -> list[dict[str, object]]:
        return self.repo.list_all()

    def create_task(self, title: str, owner_id: int) -> dict[str, object]:
        # TODO: создать задачу через TaskRepository.
        return {'id': 0, 'title': 'TODO', 'owner_id': 0}

    def get_task(self, task_id: int) -> dict[str, object]:
        task = self.repo.get_by_id(task_id)
        if task is None:
            raise HTTPException(
                status_code=404,
                detail={'detail': 'task not found', 'code': 'task_not_found'},
            )
        return task


settings = AppSettings()
user_repo = UserRepository()
task_repo = TaskRepository()
user_service = UserService(user_repo)
task_service = TaskService(task_repo)
app = FastAPI(title=settings.app_name)


@app.exception_handler(HTTPException)
async def handle_http_exception(_: Request, exc: HTTPException):
    if isinstance(exc.detail, dict):
        return JSONResponse(status_code=exc.status_code, content=exc.detail)
    return JSONResponse(status_code=exc.status_code, content={'detail': exc.detail})


@app.get('/health')
def health() -> dict[str, str]:
    return {'status': 'ok'}


@app.get(f'{settings.api_prefix}/users')
def list_users() -> list[dict[str, object]]:
    return user_service.list_users()


@app.post(f'{settings.api_prefix}/users', status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate) -> dict[str, object]:
    return user_service.create_user(payload.name)


@app.get(f'{settings.api_prefix}/tasks')
def list_tasks() -> list[dict[str, object]]:
    return task_service.list_tasks()


@app.post(f'{settings.api_prefix}/tasks', status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate) -> dict[str, object]:
    return task_service.create_task(payload.title, payload.owner_id)


@app.get(f'{settings.api_prefix}/tasks/{{task_id}}')
def get_task(task_id: int) -> dict[str, object]:
    return task_service.get_task(task_id)


def run_smoke_checks() -> None:
    client = TestClient(app)

    response = client.get('/health')
    assert response.status_code == 200, 'health endpoint should return 200 OK'

    response = client.post('/api/v1/users', json={'name': 'Anna'})
    assert response.status_code == 201, 'POST /users should return 201 Created'
    assert response.json() == {'id': 1, 'name': 'Anna'}, 'created user payload is incorrect'

    response = client.post('/api/v1/tasks', json={'title': 'Prepare demo', 'owner_id': 1})
    assert response.status_code == 201, 'POST /tasks should return 201 Created'
    assert response.json() == {'id': 1, 'title': 'Prepare demo', 'owner_id': 1}, 'created task payload is incorrect'

    response = client.get('/api/v1/tasks/1')
    assert response.status_code == 200, 'GET /tasks/1 should return created task'
    assert response.json() == {'id': 1, 'title': 'Prepare demo', 'owner_id': 1}, 'task payload is incorrect'

    response = client.get('/api/v1/tasks/999')
    assert response.status_code == 404, 'missing task should return 404 Not Found'
    assert response.json() == {'detail': 'task not found', 'code': 'task_not_found'}, 'missing task contract is incorrect'


if __name__ == '__main__':
    try:
        run_smoke_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Mini-project smoke checks passed')
