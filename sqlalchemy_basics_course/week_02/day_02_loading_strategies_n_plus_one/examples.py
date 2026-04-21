import os

from sqlalchemy import ForeignKey, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, joinedload, mapped_column, relationship

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+psycopg://postgres:postgres@localhost:5432/zero_to_qa')


class Base(DeclarativeBase):
    pass


class Project(Base):
    __tablename__ = 'sa_w2d2_projects'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    tasks: Mapped[list['Task']] = relationship(back_populates='project')


class Task(Base):
    __tablename__ = 'sa_w2d2_tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(80))
    project_id: Mapped[int] = mapped_column(ForeignKey('sa_w2d2_projects.id'))
    project: Mapped[Project] = relationship(back_populates='tasks')


def main() -> None:
    engine = create_engine(DATABASE_URL, echo=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        project = Project(name='Portal')
        project.tasks.extend([Task(title='Login page'), Task(title='Checkout')])
        session.add(project)
        session.commit()

        stmt = select(Project).options(joinedload(Project.tasks))
        rows = session.execute(stmt).unique().scalars().all()
        print('Loaded ->', [(row.name, [task.title for task in row.tasks]) for row in rows])


if __name__ == '__main__':
    main()
