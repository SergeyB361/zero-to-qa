from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Task


class TaskRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, *, title: str, description: str | None, assignee_id: int | None, created_by: int) -> Task:
        task = Task(
            title=title,
            description=description,
            status="open",
            assignee_id=assignee_id,
            created_by=created_by,
        )
        self.session.add(task)
        self.session.flush()
        return task

    def list_tasks(self) -> list[Task]:
        stmt = select(Task).order_by(Task.id)
        return list(self.session.execute(stmt).scalars().all())

    def get_task(self, task_id: int) -> Task | None:
        return self.session.get(Task, task_id)
