"""
Практическое задание:
1. Оформи связь `Project -> Build` как one-to-many.
2. Сохрани проект с двумя builds.
3. Верни имя проекта и список build statuses.

Например:
- `{'project': 'Payments', 'builds': ['green', 'red']}`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

import os

from sqlalchemy import ForeignKey, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+psycopg://postgres:postgres@localhost:5432/zero_to_qa')


class Base(DeclarativeBase):
    pass


class Project(Base):
    __tablename__ = 'sa_day4_projects'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    builds: Mapped[list['Build']] = relationship(back_populates='project')


class Build(Base):
    __tablename__ = 'sa_day4_builds'

    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str] = mapped_column(String(20))
    project_id: Mapped[int] = mapped_column(ForeignKey('sa_day4_projects.id'))
    project: Mapped[Project] = relationship(back_populates='builds')


def run_flow() -> dict[str, object]:
    engine = create_engine(DATABASE_URL, echo=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        # TODO: сохрани project с двумя builds и верни агрегированный результат.
        return {'project': 'TODO', 'builds': []}


def run_checks() -> None:
    result = run_flow()
    assert result == {'project': 'Payments', 'builds': ['green', 'red']}, 'relationship flow should persist project and two related builds'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
