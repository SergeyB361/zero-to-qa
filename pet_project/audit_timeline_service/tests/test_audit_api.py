from datetime import UTC, datetime

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker

from app.db import Base, get_session
from app.main import app


def build_client():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
        future=True,
    )
    TestingSessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True, expire_on_commit=False)
    Base.metadata.create_all(bind=engine)

    def override_session():
        session = TestingSessionLocal()
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_session] = override_session
    return TestClient(app)


def test_event_timeline_and_snapshot() -> None:
    client = build_client()
    created_at = datetime.now(UTC).isoformat()

    created = client.post(
        "/events",
        json={
            "event_id": "evt-1",
            "event_type": "task.created",
            "entity_type": "task",
            "entity_id": 1,
            "actor_id": 10,
            "occurred_at": created_at,
            "payload": {
                "title": "Investigate flaky checkout",
                "description": "capture logs",
                "status": "open",
                "assignee_id": 20,
                "created_by": 10,
            },
        },
    )
    assert created.status_code == 201

    status_changed = client.post(
        "/events",
        json={
            "event_id": "evt-2",
            "event_type": "task.status_changed",
            "entity_type": "task",
            "entity_id": 1,
            "actor_id": 11,
            "occurred_at": datetime.now(UTC).isoformat(),
            "payload": {"old_status": "open", "new_status": "done"},
        },
    )
    assert status_changed.status_code == 201

    timeline = client.get("/timeline/tasks/1")
    assert timeline.status_code == 200
    assert len(timeline.json()) == 2

    by_actor = client.get("/timeline/users/11")
    assert by_actor.status_code == 200
    assert by_actor.json()[0]["event_type"] == "task.status_changed"

    snapshot = client.get("/snapshot/tasks/1")
    assert snapshot.status_code == 200
    assert snapshot.json()["status"] == "done"
    assert snapshot.json()["title"] == "Investigate flaky checkout"
