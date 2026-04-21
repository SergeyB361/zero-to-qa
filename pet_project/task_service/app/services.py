from datetime import UTC, datetime
from uuid import uuid4

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .event_client import AuditEventClient, AuditPublishError
from .models import Task
from .repositories import TaskRepository
from .schemas import EventCreateRequest, TaskAssigneeUpdateRequest, TaskCreateRequest, TaskOut, TaskStatusUpdateRequest


class TaskService:
    def __init__(self, session: Session, publisher: AuditEventClient) -> None:
        self.session = session
        self.publisher = publisher
        self.repo = TaskRepository(session)

    def list_tasks(self) -> list[TaskOut]:
        return [TaskOut.from_orm_task(task) for task in self.repo.list_tasks()]

    def get_task(self, task_id: int) -> TaskOut:
        task = self.repo.get_task(task_id)
        if task is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="task not found")
        return TaskOut.from_orm_task(task)

    def create_task(self, payload: TaskCreateRequest) -> TaskOut:
        task = self.repo.create(
            title=payload.title,
            description=payload.description,
            assignee_id=payload.assignee_id,
            created_by=payload.actor_id,
        )
        event = self._build_event(
            event_type="task.created",
            entity_id=task.id,
            actor_id=payload.actor_id,
            payload={
                "title": task.title,
                "description": task.description,
                "status": task.status,
                "assignee_id": task.assignee_id,
                "created_by": task.created_by,
            },
        )
        self._publish_and_commit(event)
        self.session.refresh(task)
        return TaskOut.from_orm_task(task)

    def change_status(self, task_id: int, payload: TaskStatusUpdateRequest) -> TaskOut:
        task = self._require_task(task_id)
        old_status = task.status
        task.status = payload.new_status
        task.updated_at = datetime.now(UTC)
        event = self._build_event(
            event_type="task.status_changed",
            entity_id=task.id,
            actor_id=payload.actor_id,
            payload={"old_status": old_status, "new_status": payload.new_status},
        )
        self._publish_and_commit(event)
        self.session.refresh(task)
        return TaskOut.from_orm_task(task)

    def change_assignee(self, task_id: int, payload: TaskAssigneeUpdateRequest) -> TaskOut:
        task = self._require_task(task_id)
        old_assignee_id = task.assignee_id
        task.assignee_id = payload.new_assignee_id
        task.updated_at = datetime.now(UTC)
        event = self._build_event(
            event_type="task.assignee_changed",
            entity_id=task.id,
            actor_id=payload.actor_id,
            payload={"old_assignee_id": old_assignee_id, "new_assignee_id": payload.new_assignee_id},
        )
        self._publish_and_commit(event)
        self.session.refresh(task)
        return TaskOut.from_orm_task(task)

    def delete_task(self, task_id: int, actor_id: int) -> TaskOut:
        task = self._require_task(task_id)
        task.is_deleted = True
        task.updated_at = datetime.now(UTC)
        event = self._build_event(
            event_type="task.deleted",
            entity_id=task.id,
            actor_id=actor_id,
            payload={"is_deleted": True},
        )
        self._publish_and_commit(event)
        self.session.refresh(task)
        return TaskOut.from_orm_task(task)

    def _require_task(self, task_id: int) -> Task:
        task = self.repo.get_task(task_id)
        if task is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="task not found")
        return task

    def _build_event(self, *, event_type: str, entity_id: int, actor_id: int, payload: dict[str, object]) -> EventCreateRequest:
        return EventCreateRequest(
            event_id=str(uuid4()),
            event_type=event_type,
            entity_type="task",
            entity_id=entity_id,
            actor_id=actor_id,
            occurred_at=datetime.now(UTC),
            payload=payload,
        )

    def _publish_and_commit(self, event: EventCreateRequest) -> None:
        try:
            self.publisher.publish(event)
        except AuditPublishError as exc:
            self.session.rollback()
            raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=str(exc)) from exc
        self.session.commit()
