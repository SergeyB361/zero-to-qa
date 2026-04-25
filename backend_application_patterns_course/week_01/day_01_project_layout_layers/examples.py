from fastapi import APIRouter, FastAPI, status
from fastapi.testclient import TestClient
from pydantic import BaseModel


class TicketCreate(BaseModel):
    title: str


class TicketRepository:
    def __init__(self) -> None:
        self._items = [{'id': 1, 'title': 'Seed ticket'}]

    def list_all(self) -> list[dict[str, object]]:
        return list(self._items)

    def create(self, title: str) -> dict[str, object]:
        item = {'id': len(self._items) + 1, 'title': title}
        self._items.append(item)
        return item


class TicketService:
    def __init__(self, repo: TicketRepository) -> None:
        self.repo = repo

    def list_tickets(self) -> list[dict[str, object]]:
        return self.repo.list_all()

    def create_ticket(self, title: str) -> dict[str, object]:
        return self.repo.create(title)


def build_app() -> FastAPI:
    repo = TicketRepository()
    service = TicketService(repo)
    router = APIRouter(prefix='/tickets', tags=['tickets'])

    @router.get('')
    def list_tickets() -> list[dict[str, object]]:
        return service.list_tickets()

    @router.post('', status_code=status.HTTP_201_CREATED)
    def create_ticket(payload: TicketCreate) -> dict[str, object]:
        return service.create_ticket(payload.title)

    app = FastAPI(title='Project Layout Example')
    app.include_router(router)
    return app


if __name__ == '__main__':
    client = TestClient(build_app())
    print('GET /tickets ->', client.get('/tickets').json())
    created = client.post('/tickets', json={'title': 'Billing bug'})
    print('POST /tickets ->', created.status_code, created.json())
    print('GET /tickets after create ->', client.get('/tickets').json())
