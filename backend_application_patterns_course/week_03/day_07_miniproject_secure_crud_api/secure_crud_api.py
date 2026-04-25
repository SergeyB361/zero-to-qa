"""
Практическое задание:
1. Собери secure CRUD API с auth, role checks, partial update и soft delete.
2. Viewer должен читать, manager должен писать.
3. После soft delete проект должен исчезать из обычного чтения.

Например:
- без API key `GET /projects` -> `401`
- manager `POST /projects` -> `201`, `{"id": 1, "name": "Portal", "status": "draft"}`
- viewer `POST /projects` -> `403`
- `DELETE /projects/1` -> `204`, после чего `GET /projects/1` -> `404`

Критерий готовности: `run_smoke_checks()` проходит без ошибок.
"""

from dataclasses import dataclass

from fastapi import Depends, FastAPI, Header, HTTPException, Response, status
from fastapi.testclient import TestClient
from pydantic import BaseModel
from sqlalchemy import Boolean, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker
from sqlalchemy.pool import StaticPool


@dataclass(slots=True)
class AppSettings:
    database_url: str = 'sqlite+pysqlite:///:memory:'


@dataclass(slots=True)
class ActorContext:
    actor_id: str
    role: str


TOKENS = {
    'viewer-token': ActorContext(actor_id='nik', role='viewer'),
    'manager-token': ActorContext(actor_id='mila', role='manager'),
}


class Base(DeclarativeBase):
    pass


class Project(Base):
    __tablename__ = 'bap_w3d7_projects'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True)
    status: Mapped[str] = mapped_column(String(30), default='draft')
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)


class ProjectCreate(BaseModel):
    name: str
    status: str = 'draft'


class ProjectUpdate(BaseModel):
    name: str | None = None
    status: str | None = None


class ProjectNotFoundError(RuntimeError):
    pass


class ProjectRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def list_visible(self) -> list[Project]:
        return self.session.execute(
            select(Project).where(Project.is_deleted.is_(False)).order_by(Project.id)
        ).scalars().all()

    def get_visible(self, project_id: int) -> Project | None:
        return self.session.execute(
            select(Project).where(Project.id == project_id, Project.is_deleted.is_(False))
        ).scalar_one_or_none()

    def create(self, name: str, status_value: str) -> Project:
        project = Project(name=name, status=status_value, is_deleted=False)
        self.session.add(project)
        return project


class ProjectService:
    def __init__(self, repo: ProjectRepository, session: Session) -> None:
        self.repo = repo
        self.session = session

    def list_projects(self) -> list[dict[str, object]]:
        rows = self.repo.list_visible()
        return [{'id': row.id, 'name': row.name, 'status': row.status} for row in rows]

    def get_project(self, project_id: int) -> dict[str, object]:
        row = self.repo.get_visible(project_id)
        if row is None:
            raise ProjectNotFoundError('project not found')
        return {'id': row.id, 'name': row.name, 'status': row.status}

    def create_project(self, name: str, status_value: str) -> dict[str, object]:
        # TODO: создать проект через repository, сделать commit/refresh и вернуть payload.
        return {'id': 0, 'name': 'TODO', 'status': 'TODO'}

    def patch_project(self, project_id: int, payload: dict[str, object]) -> dict[str, object]:
        row = self.repo.get_visible(project_id)
        if row is None:
            raise ProjectNotFoundError('project not found')
        # TODO: применить partial update только по переданным полям и вернуть payload.
        return {'id': row.id, 'name': row.name, 'status': row.status}

    def soft_delete_project(self, project_id: int) -> None:
        row = self.repo.get_visible(project_id)
        if row is None:
            raise ProjectNotFoundError('project not found')
        # TODO: сделать soft delete через изменение ORM-модели и commit.


def build_engine(settings: AppSettings):
    return create_engine(
        settings.database_url,
        future=True,
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )


def build_session_factory(settings: AppSettings) -> sessionmaker[Session]:
    engine = build_engine(settings)
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine, expire_on_commit=False, future=True)


def create_app() -> FastAPI:
    settings = AppSettings()
    SessionLocal = build_session_factory(settings)
    app = FastAPI(title='Backend Patterns Week 3 Day 7')

    def get_actor_context(x_api_key: str | None = Header(default=None)) -> ActorContext:
        if x_api_key is None:
            raise HTTPException(status_code=401, detail='missing api key')
        actor = TOKENS.get(x_api_key)
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

    def get_repo(session: Session = Depends(get_session)) -> ProjectRepository:
        return ProjectRepository(session)

    def get_service(
        session: Session = Depends(get_session),
        repo: ProjectRepository = Depends(get_repo),
    ) -> ProjectService:
        return ProjectService(repo, session)

    @app.get('/health')
    def health() -> dict[str, str]:
        return {'status': 'ok'}

    @app.get('/projects')
    def list_projects(
        _: ActorContext = Depends(get_actor_context),
        service: ProjectService = Depends(get_service),
    ) -> list[dict[str, object]]:
        return service.list_projects()

    @app.get('/projects/{project_id}')
    def get_project(
        project_id: int,
        _: ActorContext = Depends(get_actor_context),
        service: ProjectService = Depends(get_service),
    ) -> dict[str, object]:
        try:
            return service.get_project(project_id)
        except ProjectNotFoundError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc

    @app.post('/projects', status_code=status.HTTP_201_CREATED)
    def create_project(
        payload: ProjectCreate,
        _: ActorContext = Depends(require_manager),
        service: ProjectService = Depends(get_service),
    ) -> dict[str, object]:
        return service.create_project(payload.name, payload.status)

    @app.patch('/projects/{project_id}')
    def patch_project(
        project_id: int,
        payload: ProjectUpdate,
        _: ActorContext = Depends(require_manager),
        service: ProjectService = Depends(get_service),
    ) -> dict[str, object]:
        try:
            return service.patch_project(project_id, payload.model_dump(exclude_unset=True))
        except ProjectNotFoundError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc

    @app.delete('/projects/{project_id}', status_code=status.HTTP_204_NO_CONTENT)
    def delete_project(
        project_id: int,
        _: ActorContext = Depends(require_manager),
        service: ProjectService = Depends(get_service),
    ) -> Response:
        try:
            service.soft_delete_project(project_id)
        except ProjectNotFoundError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return app


def run_smoke_checks() -> None:
    client = TestClient(create_app())

    response = client.get('/projects')
    assert response.status_code == 401, 'missing api key should return 401 on protected list route'

    response = client.post('/projects', headers={'X-API-Key': 'viewer-token'}, json={'name': 'Portal'})
    assert response.status_code == 403, 'viewer should not be able to create project'

    response = client.post('/projects', headers={'X-API-Key': 'manager-token'}, json={'name': 'Portal'})
    assert response.status_code == 201, 'manager should be able to create project'
    assert response.json() == {'id': 1, 'name': 'Portal', 'status': 'draft'}, 'created project payload is incorrect'

    response = client.get('/projects', headers={'X-API-Key': 'viewer-token'})
    assert response.status_code == 200, 'viewer should be able to read projects'
    assert response.json() == [{'id': 1, 'name': 'Portal', 'status': 'draft'}], 'project list payload is incorrect'

    response = client.patch('/projects/1', headers={'X-API-Key': 'manager-token'}, json={'status': 'active'})
    assert response.status_code == 200, 'manager should be able to patch project'
    assert response.json() == {'id': 1, 'name': 'Portal', 'status': 'active'}, 'patched project payload is incorrect'

    response = client.delete('/projects/1', headers={'X-API-Key': 'manager-token'})
    assert response.status_code == 204, 'manager should be able to soft-delete project'

    response = client.get('/projects/1', headers={'X-API-Key': 'viewer-token'})
    assert response.status_code == 404, 'soft-deleted project should disappear from normal read contract'
    assert response.json() == {'detail': 'project not found'}, 'soft-deleted project detail is incorrect'


if __name__ == '__main__':
    try:
        run_smoke_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Mini-project smoke checks passed')
