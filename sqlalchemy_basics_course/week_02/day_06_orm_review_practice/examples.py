import os

from sqlalchemy import ForeignKey, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship, selectinload

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+psycopg://postgres:postgres@localhost:5432/zero_to_qa')


class Base(DeclarativeBase):
    pass


class Suite(Base):
    __tablename__ = 'sa_w2d6_suites'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40))
    cases: Mapped[list['Case']] = relationship(back_populates='suite')


class Case(Base):
    __tablename__ = 'sa_w2d6_cases'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(80))
    suite_id: Mapped[int] = mapped_column(ForeignKey('sa_w2d6_suites.id'))
    suite: Mapped[Suite] = relationship(back_populates='cases')


def main() -> None:
    engine = create_engine(DATABASE_URL, echo=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        suite = Suite(name='API smoke')
        suite.cases.extend([Case(title='health ok'), Case(title='login works')])
        session.add(suite)
        session.commit()

        stmt = select(Suite).options(selectinload(Suite.cases))
        rows = session.execute(stmt).scalars().all()
        print('Review ->', [(row.name, [case.title for case in row.cases]) for row in rows])


if __name__ == '__main__':
    main()
