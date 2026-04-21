import os

from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+psycopg://postgres:postgres@localhost:5432/zero_to_qa')


class Base(DeclarativeBase):
    pass


class Incident(Base):
    __tablename__ = 'sa_day5_incidents'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(80))
    severity: Mapped[str] = mapped_column(String(20))


def main() -> None:
    engine = create_engine(DATABASE_URL, echo=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        session.add_all([
            Incident(title='Login 500', severity='critical'),
            Incident(title='Wrong total', severity='major'),
            Incident(title='Theme glitch', severity='minor'),
        ])
        session.commit()

        stmt = select(Incident).where(Incident.severity != 'minor').order_by(Incident.title)
        rows = session.execute(stmt).scalars().all()
        print('Filtered ->', [(row.title, row.severity) for row in rows])


if __name__ == '__main__':
    main()
