from fastapi import Depends, FastAPI, Header
from fastapi.testclient import TestClient


class ReportRepository:
    def __init__(self) -> None:
        self._items = [
            {'id': 1, 'status': 'open'},
            {'id': 2, 'status': 'closed'},
            {'id': 3, 'status': 'open'},
        ]

    def count_open(self) -> int:
        return sum(1 for item in self._items if item['status'] == 'open')


class ReportService:
    def __init__(self, repo: ReportRepository) -> None:
        self.repo = repo

    def build_summary(self, actor_id: int) -> dict[str, object]:
        return {'actor_id': actor_id, 'open_count': self.repo.count_open()}


repo = ReportRepository()


def get_repo() -> ReportRepository:
    return repo


def get_service(repo: ReportRepository = Depends(get_repo)) -> ReportService:
    return ReportService(repo)


def get_actor_id(x_actor_id: int = Header(..., alias='X-Actor-Id')) -> int:
    return x_actor_id


app = FastAPI(title='Dependency Boundaries Example')


@app.get('/reports/open-count')
def open_count(
    actor_id: int = Depends(get_actor_id),
    service: ReportService = Depends(get_service),
) -> dict[str, object]:
    return service.build_summary(actor_id)


if __name__ == '__main__':
    client = TestClient(app)
    response = client.get('/reports/open-count', headers={'X-Actor-Id': '42'})
    print(response.status_code, response.json())
