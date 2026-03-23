RETRYABLE_STATUSES = {502, 503, 504}


def should_retry(status_code: int) -> bool:
    return status_code in RETRYABLE_STATUSES


def is_idempotent(method: str) -> bool:
    return method.upper() in {"GET", "PUT", "DELETE"}


if __name__ == "__main__":
    print(should_retry(503))
    print(is_idempotent("POST"))
