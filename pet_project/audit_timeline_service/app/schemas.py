from datetime import datetime
from typing import Any

from pydantic import BaseModel


class HealthOut(BaseModel):
    status: str


class EventCreateRequest(BaseModel):
    event_id: str
    event_type: str
    entity_type: str
    entity_id: int
    actor_id: int
    occurred_at: datetime
    payload: dict[str, Any]


class EventOut(EventCreateRequest):
    pass


class TaskSnapshotOut(BaseModel):
    task_id: int
    title: str | None
    description: str | None
    status: str | None
    assignee_id: int | None
    created_by: int | None
    is_deleted: bool
    last_event_at: datetime
