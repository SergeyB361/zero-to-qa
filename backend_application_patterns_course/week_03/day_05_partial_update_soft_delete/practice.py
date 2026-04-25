"""
Практическое задание:
1. Реализуй `PATCH` через partial update внутри service layer, а не в route.
2. Реализуй `DELETE` как soft delete.
3. Спрячь soft-deleted записи из обычного list/get контракта.

Например:
- `PATCH /tasks/1` с `{"status": "done"}` -> обновляется только status
- `DELETE /tasks/2` -> `204`, но запись не удаляется физически, а помечается deleted
- после delete `GET /tasks` не должен возвращать task `2`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

from dataclasses import dataclass

from fastapi import Depends, FastAPI, HTTPException, Response, status
from fastapi.testclient import TestClient
from pydantic import BaseModel


class TaskUpdate(BaseModel):
    title: str | None = None
    status: str | None = None


@dataclass(slots=True)
class TaskRecord:
    id: int
    title: str
    status: str
    is_deleted: bool = False


class TaskNotFoundError(RuntimeError):
    pass


class InMemoryTaskRepository:
    def __init__(self, rows: list[TaskRecord]) -> None:
        self.rows = rows

    def list_visible(self) -> list[TaskRecord]:
        return [row for row in self.rows if not row.is_deleted]

    def get_visible(self, task_id: int) -> TaskRecord | None:
        return next((row for row in self.rows if row.id == task_id and not row.is_deleted), None)


class TaskService:
    def __init__(self, repo: InMemoryTaskRepository) -> None:
        self.repo = repo

    def list_tasks(self) -> list[dict[str, object]]:
        return [
            {'id': row.id, 'title': row.title, 'status': row.status}
            for row in self.repo.list_visible()
        ]

    def patch_task(self, task_id: int, payload: dict[str, object]) -> dict[str, object]:
        row = self.repo.get_visible(task_id)
        if row is None:
            raise TaskNotFoundError('task not found')
        # TODO: взять только переданные поля и обновить row внутри service layer.
        return {'id': row.id, 'title': row.title, 'status': row.status}

    def soft_delete_task(self, task_id: int) -> None:
        row = self.repo.get_visible(task_id)
        if row is None:
            raise TaskNotFoundError('task not found')
        # TODO: реализовать soft delete вместо физического удаления.
        row.is_deleted = False


def create_app() -> FastAPI:
    repo = InMemoryTaskRepository([
        TaskRecord(id=1, title='write docs', status='new'),
        TaskRecord(id=2, title='check smoke', status='open'),
    ])
    app = FastAPI(title='Backend Patterns Week 3 Day 5 Practice')

    def get_service() -> TaskService:
        return TaskService(repo)

    @app.get('/tasks')
    def list_tasks(service: TaskService = Depends(get_service)) -> list[dict[str, object]]:
        return service.list_tasks()

    @app.patch('/tasks/{task_id}')
    def patch_task(
        task_id: int,
        payload: TaskUpdate,
        service: TaskService = Depends(get_service),
    ) -> dict[str, object]:
        try:
            return service.patch_task(task_id, payload.model_dump(exclude_unset=True))
        except TaskNotFoundError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc

    @app.delete('/tasks/{task_id}', status_code=status.HTTP_204_NO_CONTENT)
    def soft_delete_task(
        task_id: int,
        service: TaskService = Depends(get_service),
    ) -> Response:
        try:
            service.soft_delete_task(task_id)
        except TaskNotFoundError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return app


def run_checks() -> None:
    client = TestClient(create_app())

    response = client.patch('/tasks/1', json={'status': 'done'})
    assert response.status_code == 200, 'patch route should return 200'
    assert response.json() == {'id': 1, 'title': 'write docs', 'status': 'done'}, 'partial update payload is incorrect'

    response = client.delete('/tasks/2')
    assert response.status_code == 204, 'soft delete route should return 204'

    response = client.get('/tasks')
    assert response.json() == [
        {'id': 1, 'title': 'write docs', 'status': 'done'}
    ], 'soft-deleted task should disappear from list endpoint'

    response = client.patch('/tasks/2', json={'status': 'reopened'})
    assert response.status_code == 404, 'soft-deleted task should not be patchable via normal route'
    assert response.json() == {'detail': 'task not found'}, 'soft-deleted get/patch contract is incorrect'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
