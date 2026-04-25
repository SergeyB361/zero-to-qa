from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.testclient import TestClient
from pydantic import BaseModel


class ProjectCreate(BaseModel):
    slug: str


class ProjectConflictError(RuntimeError):
    pass


class ProjectRepository:
    def __init__(self) -> None:
        self._items = [{'id': 1, 'slug': 'portal'}]

    def exists_by_slug(self, slug: str) -> bool:
        return any(item['slug'] == slug for item in self._items)

    def create(self, slug: str) -> dict[str, object]:
        item = {'id': len(self._items) + 1, 'slug': slug}
        self._items.append(item)
        return item


class ProjectService:
    def __init__(self, repo: ProjectRepository) -> None:
        self.repo = repo

    def create_project(self, slug: str) -> dict[str, object]:
        if self.repo.exists_by_slug(slug):
            raise ProjectConflictError('project slug already exists')
        return self.repo.create(slug)


repo = ProjectRepository()
service = ProjectService(repo)
app = FastAPI(title='Error Contracts Example')


@app.exception_handler(ProjectConflictError)
async def handle_project_conflict(_: Request, exc: ProjectConflictError) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={'detail': str(exc), 'code': 'project_conflict'},
    )


@app.post('/projects', status_code=status.HTTP_201_CREATED)
def create_project(payload: ProjectCreate) -> dict[str, object]:
    return service.create_project(payload.slug)


if __name__ == '__main__':
    client = TestClient(app)
    print(client.post('/projects', json={'slug': 'billing'}).status_code)
    duplicate = client.post('/projects', json={'slug': 'portal'})
    print(duplicate.status_code, duplicate.json())
