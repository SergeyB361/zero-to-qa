def build_bearer_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}

def build_basic_auth(username: str, password: str) -> tuple[str, str]:
    return username, password
