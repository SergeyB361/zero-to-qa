import os

from sqlalchemy import Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+psycopg://postgres:postgres@localhost:5432/zero_to_qa')


class Base(DeclarativeBase):
    pass


class Counter(Base):
    __tablename__ = 'sa_w2d1_counters'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40), unique=True)
    value: Mapped[int] = mapped_column(Integer)


def main() -> None:
    engine = create_engine(DATABASE_URL, echo=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        session.add(Counter(name='jobs', value=1))
        session.commit()

    with Session(engine) as session:
        counter = session.execute(select(Counter).where(Counter.name == 'jobs')).scalar_one()
        counter.value += 1
        session.commit()
        print('Committed value ->', counter.value)

    with Session(engine) as session:
        counter = session.execute(select(Counter).where(Counter.name == 'jobs')).scalar_one()
        counter.value = 999
        session.rollback()

    with Session(engine) as session:
        counter = session.execute(select(Counter).where(Counter.name == 'jobs')).scalar_one()
        print('Value after rollback ->', counter.value)


if __name__ == '__main__':
    main()
