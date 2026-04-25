"""
Практическое задание:
1. Отдавай дубли проекта как `409 Conflict`.
2. Отдавай отсутствующий проект как `404 Not Found`.
3. Держи формат ошибки согласованным: `detail + code`.

Например:
- `POST /projects` c `{"slug": "core"}` -> `201`
- повторный `POST /projects` c `{"slug": "core"}` -> `409`, `{"detail": "project slug already exists", "code": "project_conflict"}`
- `GET /projects/999` -> `404`, `{"detail": "project not found", "code": "project_not_found"}`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.testclient import TestClient
from pydantic import BaseModel


class ProjectCreate(BaseModel):
    slug: str


class ProjectConflictError(RuntimeError):
    pass


class ProjectNotFoundError(RuntimeError):
    pass


class ProjectRepository:
    def __init__(self) -> None:
        self._items = [{'id': 1, 'slug': 'portal'}]

    def create(self, slug: str) -> dict[str, object]:
        item = {'id': len(self._items) + 1, 'slug': slug}
        self._items.append(item)
        return item

    def exists_by_slug(self, slug: str) -> bool:
        return any(item['slug'] == slug for item in self._items)

    def get_by_id(self, project_id: int) -> dict[str, object] | None:
        return next((item for item in self._items if item['id'] == project_id), None)


class ProjectService:
    def __init__(self, repo: ProjectRepository) -> None:
        self.repo = repo

    def create_project(self, slug: str) -> dict[str, object]:
        # TODO: поднять ProjectConflictError при duplicate slug.
        return self.repo.create(slug)

    def get_project(self, project_id: int) -> dict[str, object]:
        project = self.repo.get_by_id(project_id)
        # TODO: поднять ProjectNotFoundError, если project отсутствует.
        return {'id': 0, 'slug': 'TODO'} if project is None else project


app = FastAPI(title='Practice Error Contracts')
repo = ProjectRepository()
service = ProjectService(repo)


@app.exception_handler(ProjectConflictError)
async def handle_project_conflict(_: Request, exc: ProjectConflictError) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={'detail': str(exc), 'code': 'project_conflict'},
    )


@app.exception_handler(ProjectNotFoundError)
async def handle_project_not_found(_: Request, exc: ProjectNotFoundError) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={'detail': str(exc), 'code': 'project_not_found'},
    )


@app.post('/projects', status_code=status.HTTP_201_CREATED)
def create_project(payload: ProjectCreate) -> dict[str, object]:
    return service.create_project(payload.slug)


@app.get('/projects/{project_id}')
def get_project(project_id: int) -> dict[str, object]:
    return service.get_project(project_id)


def run_checks() -> None:
    client = TestClient(app)

    response = client.post('/projects', json={'slug': 'core'})
    assert response.status_code == 201, 'new project should be created with 201'
    assert response.json() == {'id': 2, 'slug': 'core'}, 'created project payload is incorrect'

    response = client.post('/projects', json={'slug': 'core'})
    assert response.status_code == 409, 'duplicate slug should return 409 Conflict'
    assert response.json() == {
        'detail': 'project slug already exists',
        'code': 'project_conflict',
    }, 'duplicate error contract is incorrect'

    response = client.get('/projects/999')
    assert response.status_code == 404, 'missing project should return 404 Not Found'
    assert response.json() == {
        'detail': 'project not found',
        'code': 'project_not_found',
    }, 'not found error contract is incorrect'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
