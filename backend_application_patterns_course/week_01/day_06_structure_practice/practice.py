"""
Практическое задание:
1. Собери маленький backend-skeleton через app factory.
2. Используй settings object, repository, service и error handler.
3. Убедись, что prefix, create/list/get и not-found ведут себя согласованно.

Например:
- `GET /api/v1/teams` -> `[{'id': 1, 'name': 'platform'}]`
- `POST /api/v1/teams` c `{"name": "qa"}` -> `201`, `{'id': 2, 'name': 'qa'}`
- `GET /api/v1/teams/2` -> `200`, `{'id': 2, 'name': 'qa'}`
- `GET /api/v1/teams/999` -> `404`, `{"detail": "team not found", "code": "team_not_found"}`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

from dataclasses import dataclass

from fastapi import Depends, FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.testclient import TestClient
from pydantic import BaseModel


@dataclass(slots=True)
class AppSettings:
    api_prefix: str = '/api/v1'


class TeamCreate(BaseModel):
    name: str


class TeamNotFoundError(RuntimeError):
    pass


class TeamRepository:
    def __init__(self) -> None:
        self._items = [{'id': 1, 'name': 'platform'}]

    def list_all(self) -> list[dict[str, object]]:
        return list(self._items)

    def get_by_id(self, team_id: int) -> dict[str, object] | None:
        return next((item for item in self._items if item['id'] == team_id), None)

    def create(self, name: str) -> dict[str, object]:
        item = {'id': len(self._items) + 1, 'name': name}
        self._items.append(item)
        return item


class TeamService:
    def __init__(self, repo: TeamRepository) -> None:
        self.repo = repo

    def list_teams(self) -> list[dict[str, object]]:
        return self.repo.list_all()

    def get_team(self, team_id: int) -> dict[str, object]:
        team = self.repo.get_by_id(team_id)
        if team is None:
            raise TeamNotFoundError('team not found')
        return team

    def create_team(self, name: str) -> dict[str, object]:
        # TODO: создать team через repository.
        return {'id': 0, 'name': 'TODO'}


def create_app() -> FastAPI:
    settings = AppSettings()
    repo = TeamRepository()

    def get_settings() -> AppSettings:
        return settings

    def get_repo() -> TeamRepository:
        return repo

    def get_service(repo: TeamRepository = Depends(get_repo)) -> TeamService:
        return TeamService(repo)

    app = FastAPI(title='Structure Practice Week 1 Day 6')

    @app.exception_handler(TeamNotFoundError)
    async def handle_team_not_found(_: Request, exc: TeamNotFoundError) -> JSONResponse:
        return JSONResponse(status_code=404, content={'detail': str(exc), 'code': 'team_not_found'})

    @app.get(f'{settings.api_prefix}/teams')
    def list_teams(service: TeamService = Depends(get_service)) -> list[dict[str, object]]:
        return service.list_teams()

    @app.get(f'{settings.api_prefix}/teams/{{team_id}}')
    def get_team(team_id: int, service: TeamService = Depends(get_service)) -> dict[str, object]:
        return service.get_team(team_id)

    @app.post(f'{settings.api_prefix}/teams', status_code=status.HTTP_201_CREATED)
    def create_team(
        payload: TeamCreate,
        service: TeamService = Depends(get_service),
        app_settings: AppSettings = Depends(get_settings),
    ) -> dict[str, object]:
        assert app_settings.api_prefix == '/api/v1'
        return service.create_team(payload.name)

    return app


def run_checks() -> None:
    client = TestClient(create_app())

    response = client.get('/api/v1/teams')
    assert response.status_code == 200, 'list route should return 200 OK'
    assert response.json() == [{'id': 1, 'name': 'platform'}], 'seed team should be visible before create'

    response = client.post('/api/v1/teams', json={'name': 'qa'})
    assert response.status_code == 201, 'create route should return 201 Created'
    assert response.json() == {'id': 2, 'name': 'qa'}, 'created team payload is incorrect'

    response = client.get('/api/v1/teams/2')
    assert response.status_code == 200, 'created team should be readable by id'
    assert response.json() == {'id': 2, 'name': 'qa'}, 'get by id should return created team'

    response = client.get('/api/v1/teams/999')
    assert response.status_code == 404, 'missing team should return 404'
    assert response.json() == {'detail': 'team not found', 'code': 'team_not_found'}, 'not-found contract is incorrect'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
