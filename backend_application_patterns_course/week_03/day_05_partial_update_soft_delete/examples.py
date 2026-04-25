from dataclasses import dataclass

from fastapi import Depends, FastAPI, HTTPException, Response, status
from fastapi.testclient import TestClient
from pydantic import BaseModel


class TicketUpdate(BaseModel):
    title: str | None = None
    status: str | None = None


@dataclass(slots=True)
class TicketRecord:
    id: int
    title: str
    status: str
    is_deleted: bool = False


class TicketNotFoundError(RuntimeError):
    pass


class InMemoryTicketRepository:
    def __init__(self, rows: list[TicketRecord]) -> None:
        self.rows = rows

    def list_visible(self) -> list[TicketRecord]:
        return [row for row in self.rows if not row.is_deleted]

    def get_visible(self, ticket_id: int) -> TicketRecord | None:
        return next((row for row in self.rows if row.id == ticket_id and not row.is_deleted), None)


class TicketService:
    def __init__(self, repo: InMemoryTicketRepository) -> None:
        self.repo = repo

    def list_tickets(self) -> list[dict[str, object]]:
        return [
            {'id': row.id, 'title': row.title, 'status': row.status}
            for row in self.repo.list_visible()
        ]

    def patch_ticket(self, ticket_id: int, payload: dict[str, object]) -> dict[str, object]:
        row = self.repo.get_visible(ticket_id)
        if row is None:
            raise TicketNotFoundError('ticket not found')

        if 'title' in payload:
            row.title = str(payload['title'])
        if 'status' in payload:
            row.status = str(payload['status'])

        return {'id': row.id, 'title': row.title, 'status': row.status}

    def soft_delete_ticket(self, ticket_id: int) -> None:
        row = self.repo.get_visible(ticket_id)
        if row is None:
            raise TicketNotFoundError('ticket not found')
        row.is_deleted = True


def create_app() -> FastAPI:
    repo = InMemoryTicketRepository([
        TicketRecord(id=1, title='login bug', status='new'),
        TicketRecord(id=2, title='profile typo', status='open'),
    ])
    app = FastAPI(title='Backend Patterns Week 3 Day 5')

    def get_service() -> TicketService:
        return TicketService(repo)

    @app.get('/tickets')
    def list_tickets(service: TicketService = Depends(get_service)) -> list[dict[str, object]]:
        return service.list_tickets()

    @app.patch('/tickets/{ticket_id}')
    def patch_ticket(
        ticket_id: int,
        payload: TicketUpdate,
        service: TicketService = Depends(get_service),
    ) -> dict[str, object]:
        try:
            return service.patch_ticket(ticket_id, payload.model_dump(exclude_unset=True))
        except TicketNotFoundError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc

    @app.delete('/tickets/{ticket_id}', status_code=status.HTTP_204_NO_CONTENT)
    def soft_delete_ticket(
        ticket_id: int,
        service: TicketService = Depends(get_service),
    ) -> Response:
        try:
            service.soft_delete_ticket(ticket_id)
        except TicketNotFoundError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return app


if __name__ == '__main__':
    client = TestClient(create_app())
    print('PATCH ->', client.patch('/tickets/1', json={'status': 'closed'}).json())
    client.delete('/tickets/2')
    print('LIST AFTER DELETE ->', client.get('/tickets').json())
