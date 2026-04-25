from dataclasses import dataclass

from fastapi import Depends, FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.testclient import TestClient
from pydantic import BaseModel


@dataclass(slots=True)
class AppSettings:
    api_prefix: str = '/api/v1'


class EnvironmentCreate(BaseModel):
    name: str


class EnvironmentNotFoundError(RuntimeError):
    pass


class EnvironmentRepository:
    def __init__(self) -> None:
        self._items = [{'id': 1, 'name': 'dev'}]

    def list_all(self) -> list[dict[str, object]]:
        return list(self._items)

    def get_by_id(self, env_id: int) -> dict[str, object] | None:
        return next((item for item in self._items if item['id'] == env_id), None)

    def create(self, name: str) -> dict[str, object]:
        item = {'id': len(self._items) + 1, 'name': name}
        self._items.append(item)
        return item


class EnvironmentService:
    def __init__(self, repo: EnvironmentRepository) -> None:
        self.repo = repo

    def list_environments(self) -> list[dict[str, object]]:
        return self.repo.list_all()

    def get_environment(self, env_id: int) -> dict[str, object]:
        item = self.repo.get_by_id(env_id)
        if item is None:
            raise EnvironmentNotFoundError('environment not found')
        return item

    def create_environment(self, name: str) -> dict[str, object]:
        return self.repo.create(name)


repo = EnvironmentRepository()
settings = AppSettings()


def get_settings() -> AppSettings:
    return settings


def get_repo() -> EnvironmentRepository:
    return repo


def get_service(repo: EnvironmentRepository = Depends(get_repo)) -> EnvironmentService:
    return EnvironmentService(repo)


app = FastAPI(title='Structure Practice Example')


@app.exception_handler(EnvironmentNotFoundError)
async def handle_environment_not_found(_: Request, exc: EnvironmentNotFoundError) -> JSONResponse:
    return JSONResponse(status_code=404, content={'detail': str(exc), 'code': 'environment_not_found'})


@app.get(f'{settings.api_prefix}/environments')
def list_environments(service: EnvironmentService = Depends(get_service)) -> list[dict[str, object]]:
    return service.list_environments()


@app.get(f'{settings.api_prefix}/environments/{{env_id}}')
def get_environment(env_id: int, service: EnvironmentService = Depends(get_service)) -> dict[str, object]:
    return service.get_environment(env_id)


@app.post(f'{settings.api_prefix}/environments', status_code=status.HTTP_201_CREATED)
def create_environment(payload: EnvironmentCreate, service: EnvironmentService = Depends(get_service)) -> dict[str, object]:
    return service.create_environment(payload.name)


if __name__ == '__main__':
    client = TestClient(app)
    print(client.get('/api/v1/environments').json())
    print(client.post('/api/v1/environments', json={'name': 'staging'}).status_code)
    print(client.get('/api/v1/environments/99').status_code, client.get('/api/v1/environments/99').json())
