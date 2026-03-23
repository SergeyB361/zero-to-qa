def build_bearer_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def is_token_expired(expires_in_seconds: int) -> bool:
    return expires_in_seconds <= 0


if __name__ == "__main__":
    print(build_bearer_headers("abc123"))
    print(is_token_expired(0))
