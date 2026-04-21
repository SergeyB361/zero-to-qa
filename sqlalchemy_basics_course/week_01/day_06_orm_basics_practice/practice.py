"""
Практическое задание:
1. Собери связку `Environment -> CheckRun`.
2. Сохрани environment с двумя check runs.
3. Верни summary в удобном Python-виде.

Например:
- `{'environment': 'staging', 'checks': ['schema-ok', 'smoke-failed']}`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

import os

from sqlalchemy import ForeignKey, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+psycopg://postgres:postgres@localhost:5432/zero_to_qa')


class Base(DeclarativeBase):
    pass


class Environment(Base):
    __tablename__ = 'sa_day6_environments'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40))
    check_runs: Mapped[list['CheckRun']] = relationship(back_populates='environment')


class CheckRun(Base):
    __tablename__ = 'sa_day6_check_runs'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(60))
    environment_id: Mapped[int] = mapped_column(ForeignKey('sa_day6_environments.id'))
    environment: Mapped[Environment] = relationship(back_populates='check_runs')


def run_flow() -> dict[str, object]:
    engine = create_engine(DATABASE_URL, echo=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        # TODO: реализуй end-to-end scenario и верни итоговый summary.
        return {'environment': 'TODO', 'checks': []}


def run_checks() -> None:
    result = run_flow()
    assert result == {'environment': 'staging', 'checks': ['schema-ok', 'smoke-failed']}, 'review practice should persist one environment and two related check runs'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
