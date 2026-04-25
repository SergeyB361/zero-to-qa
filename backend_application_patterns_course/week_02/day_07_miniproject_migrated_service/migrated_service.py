"""
Практическое задание:
1. Переведи issue service на SQLAlchemy-backed runtime.
2. Реализуй create/list/get flow через repository и service.
3. Сделай duplicate slug -> `409`, missing issue -> `404`.

Например:
- `POST /issues` с `{"title": "DB migration", "slug": "db-migration"}` -> `201`, `{"id": 1, "title": "DB migration", "slug": "db-migration", "status": "new"}`
- `GET /issues` -> список с этой issue
- `GET /issues/db-migration` -> payload issue

Критерий готовности: `run_smoke_checks()` проходит без ошибок.
"""

from dataclasses import dataclass

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.testclient import TestClient
from pydantic import BaseModel
from sqlalchemy import String, UniqueConstraint, create_engine, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker
from sqlalchemy.pool import StaticPool


@dataclass(slots=True)
class AppSettings:
    database_url: str = 'sqlite+pysqlite:///:memory:'


class Base(DeclarativeBase):
    pass


class Issue(Base):
    __tablename__ = 'bap_w2d7_issues'
    __table_args__ = (UniqueConstraint('slug', name='uq_issue_slug'),)

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(120))
    slug: Mapped[str] = mapped_column(String(120))
    status: Mapped[str] = mapped_column(String(30), default='new')


class IssueCreate(BaseModel):
    title: str
    slug: str


class IssueAlreadyExistsError(RuntimeError):
    pass


class IssueNotFoundError(RuntimeError):
    pass


class IssueRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def list_all(self) -> list[Issue]:
        return self.session.execute(select(Issue).order_by(Issue.id)).scalars().all()

    def get_by_slug(self, slug: str) -> Issue | None:
        return self.session.execute(select(Issue).where(Issue.slug == slug)).scalar_one_or_none()

    def create(self, title: str, slug: str) -> Issue:
        issue = Issue(title=title, slug=slug, status='new')
        self.session.add(issue)
        return issue


class IssueService:
    def __init__(self, repo: IssueRepository, session: Session) -> None:
        self.repo = repo
        self.session = session

    def list_issues(self) -> list[dict[str, object]]:
        rows = self.repo.list_all()
        return [
            {'id': row.id, 'title': row.title, 'slug': row.slug, 'status': row.status}
            for row in rows
        ]

    def get_issue(self, slug: str) -> dict[str, object]:
        row = self.repo.get_by_slug(slug)
        if row is None:
            raise IssueNotFoundError('issue not found')
        return {'id': row.id, 'title': row.title, 'slug': row.slug, 'status': row.status}

    def create_issue(self, title: str, slug: str) -> dict[str, object]:
        # TODO: проверить duplicate slug, создать issue через repository, сделать commit/refresh и вернуть payload.
        return {'id': 0, 'title': 'TODO', 'slug': 'TODO', 'status': 'TODO'}



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
    app = FastAPI(title='Migrated Service Week 2 Day 7')

    def get_session():
        with SessionLocal() as session:
            yield session

    def get_repo(session: Session = Depends(get_session)) -> IssueRepository:
        return IssueRepository(session)

    def get_service(
        session: Session = Depends(get_session),
        repo: IssueRepository = Depends(get_repo),
    ) -> IssueService:
        return IssueService(repo, session)

    @app.get('/health')
    def health() -> dict[str, str]:
        return {'status': 'ok'}

    @app.get('/issues')
    def list_issues(service: IssueService = Depends(get_service)) -> list[dict[str, object]]:
        return service.list_issues()

    @app.get('/issues/{slug}')
    def get_issue(slug: str, service: IssueService = Depends(get_service)) -> dict[str, object]:
        try:
            return service.get_issue(slug)
        except IssueNotFoundError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc

    @app.post('/issues', status_code=status.HTTP_201_CREATED)
    def create_issue(payload: IssueCreate, service: IssueService = Depends(get_service)) -> dict[str, object]:
        try:
            return service.create_issue(payload.title, payload.slug)
        except IssueAlreadyExistsError as exc:
            raise HTTPException(status_code=409, detail=str(exc)) from exc

    return app



def run_smoke_checks() -> None:
    client = TestClient(create_app())

    response = client.get('/health')
    assert response.status_code == 200, 'health route should return 200'
    assert response.json() == {'status': 'ok'}, 'health payload is incorrect'

    response = client.post('/issues', json={'title': 'DB migration', 'slug': 'db-migration'})
    assert response.status_code == 201, 'create issue route should return 201'
    assert response.json() == {
        'id': 1,
        'title': 'DB migration',
        'slug': 'db-migration',
        'status': 'new',
    }, 'created issue payload is incorrect'

    response = client.get('/issues')
    assert response.status_code == 200, 'list issues route should return 200'
    assert response.json() == [{
        'id': 1,
        'title': 'DB migration',
        'slug': 'db-migration',
        'status': 'new',
    }], 'list issues payload is incorrect'

    response = client.get('/issues/db-migration')
    assert response.status_code == 200, 'get issue route should return 200 for existing slug'
    assert response.json() == {
        'id': 1,
        'title': 'DB migration',
        'slug': 'db-migration',
        'status': 'new',
    }, 'get issue payload is incorrect'


if __name__ == '__main__':
    try:
        run_smoke_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Mini-project smoke checks passed')
