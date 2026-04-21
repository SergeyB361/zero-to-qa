"""
Практическое задание:
1. Сохрани несколько events.
2. Отфильтруй только `status='failed'`.
3. Отсортируй их по `name`.

Например:
- `['auth-check', 'payment-sync']`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

import os

from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+psycopg://postgres:postgres@localhost:5432/zero_to_qa')


class Base(DeclarativeBase):
    pass


class Event(Base):
    __tablename__ = 'sa_day5_events'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80))
    status: Mapped[str] = mapped_column(String(20))


def run_flow() -> list[str]:
    engine = create_engine(DATABASE_URL, echo=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        # TODO: добавь данные и верни отсортированные names только для failed events.
        return []


def run_checks() -> None:
    result = run_flow()
    assert result == ['auth-check', 'payment-sync'], 'query flow should return failed event names ordered alphabetically'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
