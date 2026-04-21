from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class HealthOut(BaseModel):
    status: str


class TaskCreateRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str | None = None
    assignee_id: int | None = None
    actor_id: int


class TaskStatusUpdateRequest(BaseModel):
    actor_id: int
    new_status: str = Field(min_length=2)


class TaskAssigneeUpdateRequest(BaseModel):
    actor_id: int
    new_assignee_id: int | None = None


class TaskOut(BaseModel):
    id: int
    title: str
    description: str | None
    status: str
    assignee_id: int | None
    created_by: int
    created_at: datetime
    updated_at: datetime
    is_deleted: bool

    @classmethod
    def from_orm_task(cls, task: Any) -> "TaskOut":
        return cls(
            id=task.id,
            title=task.title,
            description=task.description,
            status=task.status,
            assignee_id=task.assignee_id,
            created_by=task.created_by,
            created_at=task.created_at,
            updated_at=task.updated_at,
            is_deleted=task.is_deleted,
        )


class EventCreateRequest(BaseModel):
    event_id: str
    event_type: str
    entity_type: str
    entity_id: int
    actor_id: int
    occurred_at: datetime
    payload: dict[str, Any]
