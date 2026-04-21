"""
Практическое задание:
1. Опиши модель `ServiceCheck`.
2. Сделай `id` первичным ключом.
3. Сделай `name` обязательным и уникальным.
4. Сохрани и прочитай одну запись.

Например:
- created row -> `{'name': 'api-health', 'status': 'ok'}`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

import os

from sqlalchemy import String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+psycopg://postgres:postgres@localhost:5432/zero_to_qa')


class Base(DeclarativeBase):
    pass


class ServiceCheck(Base):
    __tablename__ = 'sa_day2_service_checks'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    status: Mapped[str] = mapped_column(String(20))


def run_flow() -> dict[str, object]:
    engine = create_engine(DATABASE_URL, echo=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        # TODO: сохрани и прочитай запись `api-health`.
        return {'name': 'TODO', 'status': 'TODO'}


def run_checks() -> None:
    result = run_flow()
    assert result == {'name': 'api-health', 'status': 'ok'}, 'ORM model flow should persist and return exact row payload'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
