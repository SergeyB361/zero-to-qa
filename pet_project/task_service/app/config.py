from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATABASE_URL = f"sqlite:///{BASE_DIR / 'task_service.db'}"
AUDIT_SERVICE_URL = "http://localhost:8001"
