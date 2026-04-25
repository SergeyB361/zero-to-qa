"""
Практическое задание:
1. Создай subscriber через SQLAlchemy session.
2. После commit сделай refresh и верни созданный объект.
3. При duplicate email сделай rollback и подними понятную доменную ошибку.

Например:
- первая регистрация `olga@example.com` -> `{'id': 1, 'name': 'Olga', 'email': 'olga@example.com'}`
- повторная регистрация того же email -> `DuplicateSubscriberEmailError`
- итоговый список subscribers -> только одна запись

Критерий готовности: `run_checks()` проходит без ошибок.
"""

from sqlalchemy import String, UniqueConstraint, create_engine, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker
from sqlalchemy.pool import StaticPool


class Base(DeclarativeBase):
    pass


class Subscriber(Base):
    __tablename__ = 'bap_w2d1_practice_subscribers'
    __table_args__ = (UniqueConstraint('email', name='uq_subscriber_email'),)

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(120))


engine = create_engine(
    'sqlite+pysqlite:///:memory:',
    future=True,
    connect_args={'check_same_thread': False},
    poolclass=StaticPool,
)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False, future=True)
Base.metadata.create_all(engine)


class DuplicateSubscriberEmailError(RuntimeError):
    pass


class SubscriberService:
    def __init__(self, session: Session) -> None:
        self.session = session

    def register_subscriber(self, name: str, email: str) -> dict[str, object]:
        subscriber = Subscriber(name=name, email=email)
        self.session.add(subscriber)
        # TODO: commit, refresh и вернуть payload. При IntegrityError сделать rollback и поднять DuplicateSubscriberEmailError.
        return {'id': 0, 'name': 'TODO', 'email': 'TODO'}

    def list_subscribers(self) -> list[dict[str, object]]:
        rows = self.session.execute(select(Subscriber).order_by(Subscriber.id)).scalars().all()
        return [{'id': row.id, 'name': row.name, 'email': row.email} for row in rows]


def run_checks() -> None:
    with SessionLocal() as session:
        service = SubscriberService(session)
        created = service.register_subscriber('Olga', 'olga@example.com')
        assert created == {'id': 1, 'name': 'Olga', 'email': 'olga@example.com'}, 'first registration payload is incorrect'

        try:
            service.register_subscriber('Olga 2', 'olga@example.com')
        except DuplicateSubscriberEmailError:
            pass
        else:
            raise AssertionError('duplicate email should raise DuplicateSubscriberEmailError')

        assert service.list_subscribers() == [
            {'id': 1, 'name': 'Olga', 'email': 'olga@example.com'}
        ], 'duplicate insert should not leave extra rows in DB'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
