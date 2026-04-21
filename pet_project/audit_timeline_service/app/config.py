from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATABASE_URL = f"sqlite:///{BASE_DIR / 'audit_timeline.db'}"
