"""
Практическое задание:
1. Создай task через ORM.
2. Обнови её статус до `done`.
3. Удали task и верни финальную статистику.

Например:
- `{'created': 1, 'updated_status': 'done', 'remaining': 0}`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

import os

from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+psycopg://postgres:postgres@localhost:5432/zero_to_qa')


class Base(DeclarativeBase):
    pass


class Ticket(Base):
    __tablename__ = 'sa_day3_tickets'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(80))
    status: Mapped[str] = mapped_column(String(20))


def run_flow() -> dict[str, object]:
    engine = create_engine(DATABASE_URL, echo=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        # TODO: создай ticket, обнови status, затем удали запись.
        return {'created': 0, 'updated_status': 'TODO', 'remaining': -1}


def run_checks() -> None:
    result = run_flow()
    assert result == {'created': 1, 'updated_status': 'done', 'remaining': 0}, 'CRUD flow should create, update and then fully remove the row'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
