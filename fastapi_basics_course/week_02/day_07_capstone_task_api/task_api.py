from typing import Annotated

from fastapi import Depends, FastAPI, Header, HTTPException, status
from fastapi.testclient import TestClient
from pydantic import BaseModel

app = FastAPI(title='Task API Capstone')


class TaskCreate(BaseModel):
    title: str
    assignee: str | None = None


class TaskStatusUpdate(BaseModel):
    status: str


class TaskOut(BaseModel):
    id: int
    title: str
    status: str
    assignee: str | None = None


class TaskRepository:
    def __init__(self) -> None:
        self._items = [{'id': 1, 'title': 'Prepare demo', 'status': 'open', 'assignee': 'Anna'}]

    def list_all(self) -> list[dict[str, object]]:
        return list(self._items)

    def get_by_id(self, task_id: int) -> dict[str, object] | None:
        for item in self._items:
            if item['id'] == task_id:
                return item
        return None

    def create(self, payload: dict[str, object]) -> dict[str, object]:
        item = {'id': len(self._items) + 1, 'status': 'open', **payload}
        self._items.append(item)
        return item

    def delete(self, task_id: int) -> dict[str, object] | None:
        for index, item in enumerate(self._items):
            if item['id'] == task_id:
                return self._items.pop(index)
        return None


class TaskService:
    def __init__(self, repo: TaskRepository) -> None:
        self.repo = repo

    def list_tasks(self) -> list[dict[str, object]]:
        return self.repo.list_all()

    def get_task(self, task_id: int) -> dict[str, object] | None:
        return self.repo.get_by_id(task_id)

    def create_task(self, payload: TaskCreate) -> dict[str, object]:
        return self.repo.create(payload.model_dump())

    def change_status(self, task_id: int, new_status: str) -> dict[str, object] | None:
        task = self.repo.get_by_id(task_id)
        if task is None:
            return None
        task['status'] = new_status
        return task

    def delete_task(self, task_id: int) -> dict[str, object] | None:
        return self.repo.delete(task_id)


def require_token(x_api_key: Annotated[str | None, Header()] = None) -> str:
    if x_api_key != 'task-demo-token':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='invalid api key')
    return x_api_key


repo = TaskRepository()
service = TaskService(repo)


@app.get('/tasks', response_model=list[TaskOut])
def list_tasks(_: Annotated[str, Depends(require_token)]) -> list[TaskOut]:
    return [TaskOut(**item) for item in service.list_tasks()]


@app.get('/tasks/{task_id}', response_model=TaskOut)
def get_task(task_id: int, _: Annotated[str, Depends(require_token)]) -> TaskOut:
    task = service.get_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail='task not found')
    return TaskOut(**task)


@app.post('/tasks', response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate, _: Annotated[str, Depends(require_token)]) -> TaskOut:
    return TaskOut(**service.create_task(payload))


@app.patch('/tasks/{task_id}/status', response_model=TaskOut)
def update_status(task_id: int, payload: TaskStatusUpdate, _: Annotated[str, Depends(require_token)]) -> TaskOut:
    task = service.change_status(task_id, payload.status)
    if task is None:
        raise HTTPException(status_code=404, detail='task not found')
    return TaskOut(**task)


@app.delete('/tasks/{task_id}')
def delete_task(task_id: int, _: Annotated[str, Depends(require_token)]) -> dict[str, object]:
    deleted = service.delete_task(task_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail='task not found')
    return {'deleted_id': deleted['id']}


client = TestClient(app)
HEADERS = {'x-api-key': 'task-demo-token'}


def run_smoke_checks() -> None:
    response = client.get('/tasks', headers=HEADERS)
    assert response.status_code == 200, 'expected 200 OK response'
    assert isinstance(response.json(), list), 'endpoint should return a JSON list'

    response = client.get('/tasks/1', headers=HEADERS)
    assert response.status_code == 200, 'expected 200 OK response'
    assert response.json()['title'] == 'Prepare demo', 'GET /tasks/1 should return seeded task'

    response = client.post('/tasks', headers=HEADERS, json={'title': 'Review contract', 'assignee': 'Boris'})
    assert response.status_code == 201, 'expected 201 Created response'
    created_id = response.json()['id']

    response = client.patch(f'/tasks/{created_id}/status', headers=HEADERS, json={'status': 'done'})
    assert response.status_code == 200, 'expected 200 OK response'
    assert response.json()['status'] == 'done', 'PATCH status update did not persist'

    response = client.delete(f'/tasks/{created_id}', headers=HEADERS)
    assert response.status_code == 200, 'expected 200 OK response'
    assert response.json()['deleted_id'] == created_id, 'DELETE should return id of created task'


if __name__ == '__main__':
    try:
        run_smoke_checks()
    except AssertionError as exc:
        print(f'Smoke check failed: {exc}')
        raise
    print('Task API smoke checks passed')
