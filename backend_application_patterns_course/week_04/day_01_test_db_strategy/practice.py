"""
Практическое задание:
1. Реализуй reset тестовой БД между сценариями.
2. Реализуй seed стартовых данных для тестов.
3. Покажи, что второй сценарий не видит данные первого.

Например:
- scenario 1 -> `['qa@example.com', 'api@example.com']`
- reset
- scenario 2 -> `['ops@example.com']`
- итог: во второй фазе не должно остаться email из первого сценария

Критерий готовности: `run_checks()` проходит без ошибок.
"""

from sqlalchemy import String, create_engine, delete, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker
from sqlalchemy.pool import StaticPool


class Base(DeclarativeBase):
    pass


class Member(Base):
    __tablename__ = 'bap_w4d1_members'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True)


engine = create_engine(
    'sqlite+pysqlite:///:memory:',
    future=True,
    connect_args={'check_same_thread': False},
    poolclass=StaticPool,
)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False, future=True)
Base.metadata.create_all(engine)



def reset_database(session: Session) -> None:
    # TODO: очистить таблицу members и зафиксировать изменения.
    pass



def seed_members(session: Session, emails: list[str]) -> None:
    # TODO: добавить переданные email как строки в тестовую БД.
    pass



def list_emails(session: Session) -> list[str]:
    return session.execute(select(Member.email).order_by(Member.id)).scalars().all()



def run_checks() -> None:
    with SessionLocal() as session:
        seed_members(session, ['qa@example.com', 'api@example.com'])
        assert list_emails(session) == ['qa@example.com', 'api@example.com'], 'first seeded dataset is incorrect'

        reset_database(session)
        seed_members(session, ['ops@example.com'])
        assert list_emails(session) == ['ops@example.com'], 'test DB should be clean before second scenario'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
