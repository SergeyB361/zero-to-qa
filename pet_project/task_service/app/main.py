from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, Query
from sqlalchemy.orm import Session

from .db import Base, engine, get_session
from .event_client import AuditEventClient
from .schemas import HealthOut, TaskAssigneeUpdateRequest, TaskCreateRequest, TaskOut, TaskStatusUpdateRequest
from .services import TaskService


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="Task Service", lifespan=lifespan)


def get_publisher() -> AuditEventClient:
    return AuditEventClient()


def get_task_service(
    session: Session = Depends(get_session),
    publisher: AuditEventClient = Depends(get_publisher),
) -> TaskService:
    return TaskService(session=session, publisher=publisher)


@app.get("/health", response_model=HealthOut)
def health() -> HealthOut:
    return HealthOut(status="ok")


@app.post("/tasks", response_model=TaskOut, status_code=201)
def create_task(payload: TaskCreateRequest, service: TaskService = Depends(get_task_service)) -> TaskOut:
    return service.create_task(payload)


@app.get("/tasks", response_model=list[TaskOut])
def list_tasks(service: TaskService = Depends(get_task_service)) -> list[TaskOut]:
    return service.list_tasks()


@app.get("/tasks/{task_id}", response_model=TaskOut)
def get_task(task_id: int, service: TaskService = Depends(get_task_service)) -> TaskOut:
    return service.get_task(task_id)


@app.patch("/tasks/{task_id}/status", response_model=TaskOut)
def change_status(
    task_id: int,
    payload: TaskStatusUpdateRequest,
    service: TaskService = Depends(get_task_service),
) -> TaskOut:
    return service.change_status(task_id, payload)


@app.patch("/tasks/{task_id}/assignee", response_model=TaskOut)
def change_assignee(
    task_id: int,
    payload: TaskAssigneeUpdateRequest,
    service: TaskService = Depends(get_task_service),
) -> TaskOut:
    return service.change_assignee(task_id, payload)


@app.delete("/tasks/{task_id}", response_model=TaskOut)
def delete_task(
    task_id: int,
    actor_id: int = Query(..., ge=1),
    service: TaskService = Depends(get_task_service),
) -> TaskOut:
    return service.delete_task(task_id, actor_id)
