"""
Практическое задание:
1. Собери `build_session_factory(settings)` для in-memory runtime.
2. Реализуй create-flow через repository и service.
3. На duplicate email сделай rollback и подними понятную доменную ошибку.

Например:
- первая регистрация `mila@example.com` -> `{'id': 1, 'name': 'Mila', 'email': 'mila@example.com'}`
- повторная регистрация того же email -> `DuplicateMemberEmailError`
- список members в конце -> только одна запись

Критерий готовности: `run_checks()` проходит без ошибок.
"""

from dataclasses import dataclass

from sqlalchemy import String, UniqueConstraint, create_engine, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker
from sqlalchemy.pool import StaticPool


@dataclass(slots=True)
class AppSettings:
    database_url: str = 'sqlite+pysqlite:///:memory:'


class Base(DeclarativeBase):
    pass


class Member(Base):
    __tablename__ = 'bap_w2d6_practice_members'
    __table_args__ = (UniqueConstraint('email', name='uq_member_email'),)

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(120))


class DuplicateMemberEmailError(RuntimeError):
    pass


class MemberRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, name: str, email: str) -> Member:
        member = Member(name=name, email=email)
        self.session.add(member)
        return member

    def list_all(self) -> list[dict[str, object]]:
        rows = self.session.execute(select(Member).order_by(Member.id)).scalars().all()
        return [{'id': row.id, 'name': row.name, 'email': row.email} for row in rows]



def build_session_factory(settings: AppSettings) -> sessionmaker[Session]:
    # TODO: создать engine для in-memory SQLite через StaticPool, создать таблицы и вернуть sessionmaker.
    raise NotImplementedError('build_session_factory is not implemented yet')


class MemberService:
    def __init__(self, repo: MemberRepository, session: Session) -> None:
        self.repo = repo
        self.session = session

    def register_member(self, name: str, email: str) -> dict[str, object]:
        member = self.repo.create(name, email)
        # TODO: commit, refresh и rollback -> DuplicateMemberEmailError.
        return {'id': 0, 'name': 'TODO', 'email': 'TODO'}



def run_checks() -> None:
    SessionLocal = build_session_factory(AppSettings())
    with SessionLocal() as session:
        service = MemberService(MemberRepository(session), session)
        created = service.register_member('Mila', 'mila@example.com')
        assert created == {'id': 1, 'name': 'Mila', 'email': 'mila@example.com'}, 'created member payload is incorrect'

        try:
            service.register_member('Mila 2', 'mila@example.com')
        except DuplicateMemberEmailError:
            pass
        else:
            raise AssertionError('duplicate email should raise DuplicateMemberEmailError')

        assert MemberRepository(session).list_all() == [
            {'id': 1, 'name': 'Mila', 'email': 'mila@example.com'}
        ], 'duplicate flow should leave only one member in DB'


if __name__ == '__main__':
    try:
        run_checks()
    except NotImplementedError as exc:
        print(f'Self-check failed: {exc}')
        raise
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
