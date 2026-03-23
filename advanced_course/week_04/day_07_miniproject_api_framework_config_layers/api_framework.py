import os


def load_settings() -> dict[str, str | None]:
    return {
        "base_url": os.getenv("API_BASE_URL", "https://api.example.com"),
        "token": os.getenv("API_TOKEN"),
    }


def build_headers(token: str | None) -> dict[str, str]:
    if not token:
        return {}
    return {"Authorization": f"Bearer {token}"}
