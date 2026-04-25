"""
Практическое задание:
1. Собери `one-to-many` связь между `Team` и `Ticket`.
2. Верни список teams вместе со списком titles связанных tickets.
3. Загрузи связанные данные предсказуемо через `selectinload`, а не случайным lazy-load.

Например:
- `platform` -> `['auth bug', 'dashboard error']`
- `qa` -> `['smoke checklist']`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

from sqlalchemy import ForeignKey, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship, selectinload, sessionmaker
from sqlalchemy.pool import StaticPool


class Base(DeclarativeBase):
    pass


class Team(Base):
    __tablename__ = 'bap_w2d5_practice_teams'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    tickets: Mapped[list['Ticket']] = relationship(back_populates='team', cascade='all, delete-orphan')


class Ticket(Base):
    __tablename__ = 'bap_w2d5_practice_tickets'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    team_id: Mapped[int] = mapped_column(ForeignKey('bap_w2d5_practice_teams.id'))
    team: Mapped[Team] = relationship(back_populates='tickets')


engine = create_engine(
    'sqlite+pysqlite:///:memory:',
    future=True,
    connect_args={'check_same_thread': False},
    poolclass=StaticPool,
)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False, future=True)
Base.metadata.create_all(engine)


with SessionLocal() as session:
    platform = Team(name='platform')
    qa = Team(name='qa')
    platform.tickets.extend([Ticket(title='auth bug'), Ticket(title='dashboard error')])
    qa.tickets.append(Ticket(title='smoke checklist'))
    session.add_all([platform, qa])
    session.commit()



def list_teams_with_tickets(session: Session) -> list[dict[str, object]]:
    # TODO: загрузить Team через selectinload(Team.tickets) и вернуть payload в ожидаемом формате.
    return []



def run_checks() -> None:
    with SessionLocal() as session:
        assert list_teams_with_tickets(session) == [
            {'id': 1, 'name': 'platform', 'tickets': ['auth bug', 'dashboard error']},
            {'id': 2, 'name': 'qa', 'tickets': ['smoke checklist']},
        ], 'team/ticket relationship payload is incorrect'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
