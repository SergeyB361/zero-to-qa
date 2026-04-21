"""
Практическое задание:
1. Оставь работу с ORM внутри repository.
2. Сервис должен решать: создавать report или вернуть существующий.
3. Для нового report выставляй `status='draft'`.

Например:
- первый `ensure_report('weekly')` -> `created=True`
- второй `ensure_report('weekly')` -> `created=False`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

import os

from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+psycopg://postgres:postgres@localhost:5432/zero_to_qa')


class Base(DeclarativeBase):
    pass


class Report(Base):
    __tablename__ = 'sa_w2d3_reports'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40), unique=True)
    status: Mapped[str] = mapped_column(String(20))


class ReportRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_name(self, name: str) -> Report | None:
        return self.session.execute(select(Report).where(Report.name == name)).scalar_one_or_none()

    def create(self, name: str) -> Report:
        # TODO: создай report со статусом draft.
        item = Report(name='TODO', status='TODO')
        self.session.add(item)
        return item


class ReportService:
    def __init__(self, repo: ReportRepository) -> None:
        self.repo = repo

    def ensure_report(self, name: str) -> dict[str, object]:
        existing = self.repo.get_by_name(name)
        if existing is not None:
            return {'name': existing.name, 'status': existing.status, 'created': False}
        created = self.repo.create(name)
        return {'name': created.name, 'status': created.status, 'created': True}


def run_flow() -> list[dict[str, object]]:
    engine = create_engine(DATABASE_URL, echo=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        service = ReportService(ReportRepository(session))
        first = service.ensure_report('weekly')
        session.commit()
        second = service.ensure_report('weekly')
        return [first, second]


def run_checks() -> None:
    result = run_flow()
    assert result == [
        {'name': 'weekly', 'status': 'draft', 'created': True},
        {'name': 'weekly', 'status': 'draft', 'created': False},
    ], 'repository/service practice should create once and reuse existing report afterwards'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
