import os

from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+psycopg://postgres:postgres@localhost:5432/zero_to_qa')


class Base(DeclarativeBase):
    pass


class Task(Base):
    __tablename__ = 'sa_day3_tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(80))
    status: Mapped[str] = mapped_column(String(20))


def main() -> None:
    engine = create_engine(DATABASE_URL, echo=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        task = Task(title='Check webhook', status='open')
        session.add(task)
        session.commit()

        task.status = 'done'
        session.commit()

        row = session.execute(select(Task).where(Task.id == task.id)).scalar_one()
        print('Updated ->', {'id': row.id, 'title': row.title, 'status': row.status})

        session.delete(row)
        session.commit()
        remaining = session.execute(select(Task)).scalars().all()
        print('Remaining after delete ->', len(remaining))


if __name__ == '__main__':
    main()
