"""
Практическое задание:
1. Собери `Service -> Check` one-to-many модель.
2. Сохрани сервис с двумя checks.
3. Прочитай сервис через `selectinload`.
4. Верни итоговый summary.

Например:
- `{'service': 'billing-api', 'checks': ['health', 'auth']}`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

import os

from sqlalchemy import ForeignKey, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship, selectinload

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+psycopg://postgres:postgres@localhost:5432/zero_to_qa')


class Base(DeclarativeBase):
    pass


class Service(Base):
    __tablename__ = 'sa_w2d6_services'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(60))
    checks: Mapped[list['Check']] = relationship(back_populates='service')


class Check(Base):
    __tablename__ = 'sa_w2d6_checks'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40))
    service_id: Mapped[int] = mapped_column(ForeignKey('sa_w2d6_services.id'))
    service: Mapped[Service] = relationship(back_populates='checks')


def run_flow() -> dict[str, object]:
    engine = create_engine(DATABASE_URL, echo=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        # TODO: реализуй сохранение и чтение summary через selectinload.
        return {'service': 'TODO', 'checks': []}


def run_checks() -> None:
    result = run_flow()
    assert result == {'service': 'billing-api', 'checks': ['health', 'auth']}, 'review ORM practice should persist service and two related checks'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
