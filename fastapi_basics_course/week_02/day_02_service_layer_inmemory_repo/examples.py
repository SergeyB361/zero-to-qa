from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title='FastAPI Basics Week 2 Day 2')


class ProjectCreate(BaseModel):
    name: str


class ProjectRepository:
    def __init__(self) -> None:
        self._items = [{'id': 1, 'name': 'Portal'}]

    def list_all(self) -> list[dict[str, object]]:
        return list(self._items)

    def create(self, payload: dict[str, object]) -> dict[str, object]:
        item = {'id': len(self._items) + 1, **payload}
        self._items.append(item)
        return item


class ProjectService:
    def __init__(self, repo: ProjectRepository) -> None:
        self.repo = repo

    def list_projects(self) -> list[dict[str, object]]:
        return self.repo.list_all()

    def create_project(self, name: str) -> dict[str, object]:
        return self.repo.create({'name': name})


repo = ProjectRepository()
service = ProjectService(repo)


@app.get('/projects')
def list_projects() -> list[dict[str, object]]:
    return service.list_projects()


@app.post('/projects')
def create_project(payload: ProjectCreate) -> dict[str, object]:
    return service.create_project(payload.name)
