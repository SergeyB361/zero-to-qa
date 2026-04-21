from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import DomainEvent


class EventRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, event: DomainEvent) -> DomainEvent:
        self.session.add(event)
        return event

    def list_events(self) -> list[DomainEvent]:
        stmt = select(DomainEvent).order_by(DomainEvent.occurred_at, DomainEvent.event_id)
        return list(self.session.execute(stmt).scalars().all())

    def get_event(self, event_id: str) -> DomainEvent | None:
        return self.session.get(DomainEvent, event_id)

    def list_by_task(self, task_id: int) -> list[DomainEvent]:
        stmt = (
            select(DomainEvent)
            .where(DomainEvent.entity_type == "task", DomainEvent.entity_id == task_id)
            .order_by(DomainEvent.occurred_at, DomainEvent.event_id)
        )
        return list(self.session.execute(stmt).scalars().all())

    def list_by_actor(self, actor_id: int) -> list[DomainEvent]:
        stmt = select(DomainEvent).where(DomainEvent.actor_id == actor_id).order_by(DomainEvent.occurred_at, DomainEvent.event_id)
        return list(self.session.execute(stmt).scalars().all())
