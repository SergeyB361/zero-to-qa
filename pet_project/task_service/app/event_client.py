import httpx

from .config import AUDIT_SERVICE_URL
from .schemas import EventCreateRequest


class AuditPublishError(RuntimeError):
    pass


class AuditEventClient:
    def __init__(self, base_url: str = AUDIT_SERVICE_URL) -> None:
        self.base_url = base_url.rstrip("/")

    def publish(self, event: EventCreateRequest) -> None:
        with httpx.Client(timeout=5.0) as client:
            response = client.post(f"{self.base_url}/events", json=event.model_dump(mode="json"))
        if response.status_code != 201:
            raise AuditPublishError(f"audit service returned {response.status_code}")
