"""
Практическое задание:
1. Собери service через dependency function.
2. Передай actor_id через отдельную header dependency.
3. Пусть route остаётся thin: он только вызывает service.

Например:
- `GET /dashboard/summary` с `X-Actor-Id: 7`
- ответ -> `{"actor_id": 7, "active_projects": 2}`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

from fastapi import Depends, FastAPI, Header
from fastapi.testclient import TestClient


class DashboardRepository:
    def __init__(self) -> None:
        self._projects = [
            {'id': 1, 'is_active': True},
            {'id': 2, 'is_active': True},
            {'id': 3, 'is_active': False},
        ]

    def count_active(self) -> int:
        return sum(1 for item in self._projects if item['is_active'])


class DashboardService:
    def __init__(self, repo: DashboardRepository) -> None:
        self.repo = repo

    def build_summary(self, actor_id: int) -> dict[str, object]:
        # TODO: вернуть словарь actor_id + active_projects через repo.
        return {'actor_id': 0, 'active_projects': 0}


repo = DashboardRepository()


def get_repo() -> DashboardRepository:
    return repo


def get_service(repo: DashboardRepository = Depends(get_repo)) -> DashboardService:
    # TODO: вернуть DashboardService, собранный из repo.
    return DashboardService(DashboardRepository())


def get_actor_id(x_actor_id: int = Header(..., alias='X-Actor-Id')) -> int:
    return x_actor_id


app = FastAPI(title='Practice Dependency Boundaries')


@app.get('/dashboard/summary')
def dashboard_summary(
    actor_id: int = Depends(get_actor_id),
    service: DashboardService = Depends(get_service),
) -> dict[str, object]:
    return service.build_summary(actor_id)


def run_checks() -> None:
    client = TestClient(app)

    response = client.get('/dashboard/summary', headers={'X-Actor-Id': '7'})
    assert response.status_code == 200, 'expected 200 OK for dashboard summary'
    assert response.json() == {'actor_id': 7, 'active_projects': 2}, 'summary should use header actor_id and repo data'

    response = client.get('/dashboard/summary')
    assert response.status_code == 422, 'missing required X-Actor-Id header should return 422'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
