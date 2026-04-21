import os

from sqlalchemy import ForeignKey, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship, selectinload

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+psycopg://postgres:postgres@localhost:5432/zero_to_qa')


class Base(DeclarativeBase):
    pass


class Task(Base):
    __tablename__ = 'sa_capstone_tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    status: Mapped[str] = mapped_column(String(20))
    comments: Mapped[list['TaskComment']] = relationship(back_populates='task')


class TaskComment(Base):
    __tablename__ = 'sa_capstone_task_comments'

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(200))
    task_id: Mapped[int] = mapped_column(ForeignKey('sa_capstone_tasks.id'))
    task: Mapped[Task] = relationship(back_populates='comments')


def seed_tasks(session: Session) -> None:
    # TODO: создай seeded task и базовый comment.
    pass


def add_comment(session: Session, task_id: int, text: str) -> dict[str, object]:
    # TODO: сохрани новый comment и верни его payload.
    return {'task_id': task_id, 'text': 'TODO'}


def task_summary(session: Session, task_id: int) -> dict[str, object]:
    # TODO: собери summary через ORM + selectinload.
    return {'title': 'TODO', 'comments': []}


def run_smoke_checks() -> None:
    engine = create_engine(DATABASE_URL, echo=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        seed_tasks(session)
        created = add_comment(session, 1, 'Need retry logic')
        session.commit()
        assert created == {'task_id': 1, 'text': 'Need retry logic'}, 'add_comment should return task_id/text payload'
        summary = task_summary(session, 1)
        assert summary['title'] == 'Investigate flaky checkout', 'summary should return seeded task title'
        assert 'Need retry logic' in summary['comments'], 'summary should include newly created comment text'


if __name__ == '__main__':
    try:
        run_smoke_checks()
    except AssertionError as exc:
        print(f'Smoke check failed: {exc}')
        raise
    print('Task ORM service smoke checks passed')
