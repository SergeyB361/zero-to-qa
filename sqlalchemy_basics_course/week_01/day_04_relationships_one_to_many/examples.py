import os

from sqlalchemy import ForeignKey, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+psycopg://postgres:postgres@localhost:5432/zero_to_qa')


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'sa_day4_users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    tasks: Mapped[list['Task']] = relationship(back_populates='assignee')


class Task(Base):
    __tablename__ = 'sa_day4_tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(80))
    assignee_id: Mapped[int] = mapped_column(ForeignKey('sa_day4_users.id'))
    assignee: Mapped[User] = relationship(back_populates='tasks')


def main() -> None:
    engine = create_engine(DATABASE_URL, echo=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        user = User(name='Anna')
        user.tasks.append(Task(title='Investigate 500'))
        session.add(user)
        session.commit()

        row = session.execute(select(User).where(User.name == 'Anna')).scalar_one()
        print('User ->', row.name)
        print('Tasks ->', [task.title for task in row.tasks])


if __name__ == '__main__':
    main()
