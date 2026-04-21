import os

from sqlalchemy import ForeignKey, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+psycopg://postgres:postgres@localhost:5432/zero_to_qa')


class Base(DeclarativeBase):
    pass


class Team(Base):
    __tablename__ = 'sa_day6_teams'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40))
    members: Mapped[list['Member']] = relationship(back_populates='team')


class Member(Base):
    __tablename__ = 'sa_day6_members'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40))
    team_id: Mapped[int] = mapped_column(ForeignKey('sa_day6_teams.id'))
    team: Mapped[Team] = relationship(back_populates='members')


def main() -> None:
    engine = create_engine(DATABASE_URL, echo=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        qa = Team(name='QA')
        qa.members.extend([Member(name='Anna'), Member(name='Boris')])
        session.add(qa)
        session.commit()

        rows = session.execute(select(Team)).scalars().all()
        print('Teams ->', [(team.name, [m.name for m in team.members]) for team in rows])


if __name__ == '__main__':
    main()
