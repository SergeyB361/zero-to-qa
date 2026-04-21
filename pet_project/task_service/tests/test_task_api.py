from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker

from app.db import Base, get_session
from app.main import app, get_publisher


class StubPublisher:
    def __init__(self) -> None:
        self.events: list[dict[str, object]] = []

    def publish(self, event) -> None:
        self.events.append(event.model_dump(mode="python"))


def build_client():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
        future=True,
    )
    TestingSessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True, expire_on_commit=False)
    Base.metadata.create_all(bind=engine)
    publisher = StubPublisher()

    def override_session():
        session = TestingSessionLocal()
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_session] = override_session
    app.dependency_overrides[get_publisher] = lambda: publisher
    return TestClient(app), publisher


def test_task_flow() -> None:
    client, publisher = build_client()

    created = client.post(
        "/tasks",
        json={"title": "Check snapshot", "description": "smoke", "assignee_id": 10, "actor_id": 1},
    )
    assert created.status_code == 201
    assert created.json()["status"] == "open"

    listed = client.get("/tasks")
    assert listed.status_code == 200
    assert len(listed.json()) == 1

    changed = client.patch("/tasks/1/status", json={"actor_id": 2, "new_status": "in_progress"})
    assert changed.status_code == 200
    assert changed.json()["status"] == "in_progress"

    deleted = client.delete("/tasks/1?actor_id=3")
    assert deleted.status_code == 200
    assert deleted.json()["is_deleted"] is True

    assert [event["event_type"] for event in publisher.events] == [
        "task.created",
        "task.status_changed",
        "task.deleted",
    ]
