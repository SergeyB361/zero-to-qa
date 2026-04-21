"""
Практическое задание:
1. Создай один `JobRun`.
2. Обнови его статус и зафиксируй commit.
3. Попробуй второе изменение и откати rollback.
4. Верни финальный статус из БД.

Например:
- финальный статус -> `done`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

import os

from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+psycopg://postgres:postgres@localhost:5432/zero_to_qa')


class Base(DeclarativeBase):
    pass


class JobRun(Base):
    __tablename__ = 'sa_w2d1_job_runs'

    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str] = mapped_column(String(20))


def run_flow() -> str:
    engine = create_engine(DATABASE_URL, echo=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        # TODO: реализуй commit + rollback сценарий.
        return 'TODO'


def run_checks() -> None:
    result = run_flow()
    assert result == 'done', 'final persisted status should remain done after rollback of later change'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
