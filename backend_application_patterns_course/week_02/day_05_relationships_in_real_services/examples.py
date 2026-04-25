from sqlalchemy import ForeignKey, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship, selectinload, sessionmaker
from sqlalchemy.pool import StaticPool


class Base(DeclarativeBase):
    pass


class Project(Base):
    __tablename__ = 'bap_w2d5_projects'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    tasks: Mapped[list['Task']] = relationship(back_populates='project', cascade='all, delete-orphan')


class Task(Base):
    __tablename__ = 'bap_w2d5_tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    project_id: Mapped[int] = mapped_column(ForeignKey('bap_w2d5_projects.id'))
    project: Mapped[Project] = relationship(back_populates='tasks')


engine = create_engine(
    'sqlite+pysqlite:///:memory:',
    future=True,
    connect_args={'check_same_thread': False},
    poolclass=StaticPool,
)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False, future=True)
Base.metadata.create_all(engine)


with SessionLocal() as session:
    portal = Project(name='portal')
    billing = Project(name='billing')
    portal.tasks.extend([Task(title='login check'), Task(title='profile form')])
    billing.tasks.append(Task(title='invoice rounding'))
    session.add_all([portal, billing])
    session.commit()



def list_projects_with_tasks(session: Session) -> list[dict[str, object]]:
    rows = session.execute(
        select(Project).options(selectinload(Project.tasks)).order_by(Project.id)
    ).scalars().all()
    return [
        {
            'id': row.id,
            'name': row.name,
            'tasks': [task.title for task in sorted(row.tasks, key=lambda item: item.id)],
        }
        for row in rows
    ]


if __name__ == '__main__':
    with SessionLocal() as session:
        print('PROJECTS ->', list_projects_with_tasks(session))
        task = session.execute(select(Task).where(Task.title == 'invoice rounding')).scalar_one()
        print('TASK ->', {'title': task.title, 'project': task.project.name})
