from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .models import DomainEvent
from .repositories import EventRepository
from .schemas import EventCreateRequest, EventOut, TaskSnapshotOut


class AuditService:
    def __init__(self, session: Session) -> None:
        self.session = session
        self.repo = EventRepository(session)

    def create_event(self, payload: EventCreateRequest) -> EventOut:
        event = DomainEvent(**payload.model_dump())
        self.repo.create(event)
        self.session.commit()
        return EventOut(**payload.model_dump())

    def list_events(self) -> list[EventOut]:
        return [self._to_event_out(event) for event in self.repo.list_events()]

    def get_event(self, event_id: str) -> EventOut:
        event = self.repo.get_event(event_id)
        if event is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="event not found")
        return self._to_event_out(event)

    def timeline_by_task(self, task_id: int) -> list[EventOut]:
        return [self._to_event_out(event) for event in self.repo.list_by_task(task_id)]

    def timeline_by_actor(self, actor_id: int) -> list[EventOut]:
        return [self._to_event_out(event) for event in self.repo.list_by_actor(actor_id)]

    def snapshot_by_task(self, task_id: int) -> TaskSnapshotOut:
        events = self.repo.list_by_task(task_id)
        if not events:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="task timeline not found")

        state = {
            "task_id": task_id,
            "title": None,
            "description": None,
            "status": None,
            "assignee_id": None,
            "created_by": None,
            "is_deleted": False,
            "last_event_at": events[-1].occurred_at,
        }

        for event in events:
            payload = event.payload
            if event.event_type == "task.created":
                state["title"] = payload.get("title")
                state["description"] = payload.get("description")
                state["status"] = payload.get("status")
                state["assignee_id"] = payload.get("assignee_id")
                state["created_by"] = payload.get("created_by")
                state["is_deleted"] = False
            elif event.event_type == "task.status_changed":
                state["status"] = payload.get("new_status")
            elif event.event_type == "task.assignee_changed":
                state["assignee_id"] = payload.get("new_assignee_id")
            elif event.event_type == "task.deleted":
                state["is_deleted"] = bool(payload.get("is_deleted"))
            state["last_event_at"] = event.occurred_at

        return TaskSnapshotOut(**state)

    @staticmethod
    def _to_event_out(event: DomainEvent) -> EventOut:
        return EventOut(
            event_id=event.event_id,
            event_type=event.event_type,
            entity_type=event.entity_type,
            entity_id=event.entity_id,
            actor_id=event.actor_id,
            occurred_at=event.occurred_at,
            payload=event.payload,
        )
