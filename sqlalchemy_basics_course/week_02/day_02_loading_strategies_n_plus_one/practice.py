"""
Практическое задание:
1. Сохрани один `Release` с двумя `Deploy`.
2. Прочитай данные через eager loading.
3. Верни summary без дополнительных Python-заглушек.

Например:
- `{'release': '2026.04', 'deploys': ['stage', 'prod']}`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

import os

from sqlalchemy import ForeignKey, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship, selectinload

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+psycopg://postgres:postgres@localhost:5432/zero_to_qa')


class Base(DeclarativeBase):
    pass


class Release(Base):
    __tablename__ = 'sa_w2d2_releases'

    id: Mapped[int] = mapped_column(primary_key=True)
    version: Mapped[str] = mapped_column(String(30))
    deploys: Mapped[list['Deploy']] = relationship(back_populates='release')


class Deploy(Base):
    __tablename__ = 'sa_w2d2_deploys'

    id: Mapped[int] = mapped_column(primary_key=True)
    environment: Mapped[str] = mapped_column(String(20))
    release_id: Mapped[int] = mapped_column(ForeignKey('sa_w2d2_releases.id'))
    release: Mapped[Release] = relationship(back_populates='deploys')


def run_flow() -> dict[str, object]:
    engine = create_engine(DATABASE_URL, echo=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        # TODO: сохрани release/deploys и прочитай их через selectinload.
        return {'release': 'TODO', 'deploys': []}


def run_checks() -> None:
    result = run_flow()
    assert result == {'release': '2026.04', 'deploys': ['stage', 'prod']}, 'loading strategy practice should return release with both deploy environments'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
