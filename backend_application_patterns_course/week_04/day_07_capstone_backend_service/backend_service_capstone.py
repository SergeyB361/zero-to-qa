"""
Практическое задание:
1. Собери capstone backend-service с auth, CRUD, update/delete и health route.
2. Сохрани единый стиль контрактов: `401`, `403`, `404`, `201`, `204`.
3. Сделай сервис воспроизводимым по runtime и проверяемым через smoke-check.

Например:
- `GET /health` -> `200`, `{"status": "ok"}`
- manager `POST /items` -> `201`, корректный payload
- viewer `POST /items` -> `403`
- `DELETE /items/1` -> `204`, после чего normal read должен давать `404`

Критерий готовности: `run_smoke_checks()` проходит без ошибок.
"""

import os
from dataclasses import dataclass

from fastapi import Depends, FastAPI, Header, HTTPException, Response, status
from fastapi.testclient import TestClient
from pydantic import BaseModel
from sqlalchemy import Boolean, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker
from sqlalchemy.pool import StaticPool


@dataclass(slots=True)
class AppSettings:
    database_url: str
    manager_token: str
    viewer_token: str

    @classmethod
    def from_env(cls) -> 'AppSettings':
        return cls(
            database_url=os.environ.get('DATABASE_URL', 'sqlite+pysqlite:///:memory:'),
            manager_token=os.environ.get('MANAGER_TOKEN', 'manager-token'),
            viewer_token=os.environ.get('VIEWER_TOKEN', 'viewer-token'),
        )


@dataclass(slots=True)
class ActorContext:
    actor_id: str
    role: str


class Base(DeclarativeBase):
    pass


class CatalogItem(Base):
    __tablename__ = 'bap_w4d7_items'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True)
    status: Mapped[str] = mapped_column(String(30), default='draft')
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)


class ItemCreate(BaseModel):
    name: str
    status: str = 'draft'


class ItemUpdate(BaseModel):
    name: str | None = None
    status: str | None = None


class ItemNotFoundError(RuntimeError):
    pass


class ItemRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def list_visible(self) -> list[CatalogItem]:
        return self.session.execute(
            select(CatalogItem).where(CatalogItem.is_deleted.is_(False)).order_by(CatalogItem.id)
        ).scalars().all()

    def get_visible(self, item_id: int) -> CatalogItem | None:
        return self.session.execute(
            select(CatalogItem).where(CatalogItem.id == item_id, CatalogItem.is_deleted.is_(False))
        ).scalar_one_or_none()

    def create(self, name: str, status_value: str) -> CatalogItem:
        item = CatalogItem(name=name, status=status_value, is_deleted=False)
        self.session.add(item)
        return item


class ItemService:
    def __init__(self, repo: ItemRepository, session: Session) -> None:
        self.repo = repo
        self.session = session

    def list_items(self) -> list[dict[str, object]]:
        rows = self.repo.list_visible()
        return [{'id': row.id, 'name': row.name, 'status': row.status} for row in rows]

    def get_item(self, item_id: int) -> dict[str, object]:
        row = self.repo.get_visible(item_id)
        if row is None:
            raise ItemNotFoundError('item not found')
        return {'id': row.id, 'name': row.name, 'status': row.status}

    def create_item(self, name: str, status_value: str) -> dict[str, object]:
        # TODO: создать item через repository, сделать commit/refresh и вернуть payload.
        return {'id': 0, 'name': 'TODO', 'status': 'TODO'}

    def patch_item(self, item_id: int, payload: dict[str, object]) -> dict[str, object]:
        row = self.repo.get_visible(item_id)
        if row is None:
            raise ItemNotFoundError('item not found')
        # TODO: применить partial update только по переданным полям и вернуть payload.
        return {'id': row.id, 'name': row.name, 'status': row.status}

    def soft_delete_item(self, item_id: int) -> None:
        row = self.repo.get_visible(item_id)
        if row is None:
            raise ItemNotFoundError('item not found')
        # TODO: сделать soft delete через ORM-модель и commit.


def build_engine(settings: AppSettings):
    if settings.database_url.startswith('sqlite'):
        return create_engine(
            settings.database_url,
            future=True,
            connect_args={'check_same_thread': False},
            poolclass=StaticPool,
        )
    return create_engine(settings.database_url, future=True, pool_pre_ping=True)


def build_session_factory(settings: AppSettings) -> sessionmaker[Session]:
    engine = build_engine(settings)
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine, expire_on_commit=False, future=True)


def create_app() -> FastAPI:
    settings = AppSettings.from_env()
    SessionLocal = build_session_factory(settings)
    tokens = {
        settings.viewer_token: ActorContext(actor_id='nik', role='viewer'),
        settings.manager_token: ActorContext(actor_id='mila', role='manager'),
    }
    app = FastAPI(title='Backend Patterns Week 4 Day 7 Capstone')

    def get_actor_context(x_api_key: str | None = Header(default=None)) -> ActorContext:
        if x_api_key is None:
            raise HTTPException(status_code=401, detail='missing api key')
        actor = tokens.get(x_api_key)
        if actor is None:
            raise HTTPException(status_code=401, detail='invalid api key')
        return actor

    def require_manager(actor: ActorContext = Depends(get_actor_context)) -> ActorContext:
        if actor.role != 'manager':
            raise HTTPException(status_code=403, detail='insufficient permissions')
        return actor

    def get_session():
        with SessionLocal() as session:
            yield session

    def get_repo(session: Session = Depends(get_session)) -> ItemRepository:
        return ItemRepository(session)

    def get_service(
        session: Session = Depends(get_session),
        repo: ItemRepository = Depends(get_repo),
    ) -> ItemService:
        return ItemService(repo, session)

    @app.get('/health')
    def health() -> dict[str, str]:
        return {'status': 'ok'}

    @app.get('/items')
    def list_items(
        _: ActorContext = Depends(get_actor_context),
        service: ItemService = Depends(get_service),
    ) -> list[dict[str, object]]:
        return service.list_items()

    @app.get('/items/{item_id}')
    def get_item(
        item_id: int,
        _: ActorContext = Depends(get_actor_context),
        service: ItemService = Depends(get_service),
    ) -> dict[str, object]:
        try:
            return service.get_item(item_id)
        except ItemNotFoundError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc

    @app.post('/items', status_code=status.HTTP_201_CREATED)
    def create_item(
        payload: ItemCreate,
        _: ActorContext = Depends(require_manager),
        service: ItemService = Depends(get_service),
    ) -> dict[str, object]:
        return service.create_item(payload.name, payload.status)

    @app.patch('/items/{item_id}')
    def patch_item(
        item_id: int,
        payload: ItemUpdate,
        _: ActorContext = Depends(require_manager),
        service: ItemService = Depends(get_service),
    ) -> dict[str, object]:
        try:
            return service.patch_item(item_id, payload.model_dump(exclude_unset=True))
        except ItemNotFoundError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc

    @app.delete('/items/{item_id}', status_code=status.HTTP_204_NO_CONTENT)
    def delete_item(
        item_id: int,
        _: ActorContext = Depends(require_manager),
        service: ItemService = Depends(get_service),
    ) -> Response:
        try:
            service.soft_delete_item(item_id)
        except ItemNotFoundError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return app


def run_smoke_checks() -> None:
    os.environ['DATABASE_URL'] = 'sqlite+pysqlite:///:memory:'
    os.environ['MANAGER_TOKEN'] = 'manager-token'
    os.environ['VIEWER_TOKEN'] = 'viewer-token'

    client = TestClient(create_app())

    response = client.get('/health')
    assert response.status_code == 200, 'health route should return 200'
    assert response.json() == {'status': 'ok'}, 'health payload is incorrect'

    response = client.get('/items')
    assert response.status_code == 401, 'missing api key should return 401 on protected list route'

    response = client.post('/items', headers={'X-API-Key': 'viewer-token'}, json={'name': 'Portal'})
    assert response.status_code == 403, 'viewer should not be able to create item'

    response = client.post('/items', headers={'X-API-Key': 'manager-token'}, json={'name': 'Portal'})
    assert response.status_code == 201, 'manager should be able to create item'
    assert response.json() == {'id': 1, 'name': 'Portal', 'status': 'draft'}, 'created item payload is incorrect'

    response = client.patch('/items/1', headers={'X-API-Key': 'manager-token'}, json={'status': 'active'})
    assert response.status_code == 200, 'manager should be able to patch item'
    assert response.json() == {'id': 1, 'name': 'Portal', 'status': 'active'}, 'patched item payload is incorrect'

    response = client.delete('/items/1', headers={'X-API-Key': 'manager-token'})
    assert response.status_code == 204, 'manager should be able to delete item'

    response = client.get('/items/1', headers={'X-API-Key': 'viewer-token'})
    assert response.status_code == 404, 'soft-deleted item should disappear from normal read contract'
    assert response.json() == {'detail': 'item not found'}, 'deleted item detail is incorrect'


if __name__ == '__main__':
    try:
        run_smoke_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Capstone smoke checks passed')
