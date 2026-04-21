from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from .db import Base, engine, get_session
from .schemas import EventCreateRequest, EventOut, HealthOut, TaskSnapshotOut
from .services import AuditService


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="Audit Timeline Service", lifespan=lifespan)


def get_audit_service(session: Session = Depends(get_session)) -> AuditService:
    return AuditService(session=session)


@app.get("/health", response_model=HealthOut)
def health() -> HealthOut:
    return HealthOut(status="ok")


@app.post("/events", response_model=EventOut, status_code=201)
def create_event(payload: EventCreateRequest, service: AuditService = Depends(get_audit_service)) -> EventOut:
    return service.create_event(payload)


@app.get("/events", response_model=list[EventOut])
def list_events(service: AuditService = Depends(get_audit_service)) -> list[EventOut]:
    return service.list_events()


@app.get("/events/{event_id}", response_model=EventOut)
def get_event(event_id: str, service: AuditService = Depends(get_audit_service)) -> EventOut:
    return service.get_event(event_id)


@app.get("/timeline/tasks/{task_id}", response_model=list[EventOut])
def timeline_by_task(task_id: int, service: AuditService = Depends(get_audit_service)) -> list[EventOut]:
    return service.timeline_by_task(task_id)


@app.get("/timeline/users/{actor_id}", response_model=list[EventOut])
def timeline_by_actor(actor_id: int, service: AuditService = Depends(get_audit_service)) -> list[EventOut]:
    return service.timeline_by_actor(actor_id)


@app.get("/snapshot/tasks/{task_id}", response_model=TaskSnapshotOut)
def snapshot_by_task(task_id: int, service: AuditService = Depends(get_audit_service)) -> TaskSnapshotOut:
    return service.snapshot_by_task(task_id)
