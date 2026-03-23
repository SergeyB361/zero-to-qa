RETRYABLE_CODES = {408, 429, 500, 502, 503, 504}


def should_retry(status_code: int, method: str) -> bool:
    if status_code not in RETRYABLE_CODES:
        return False
    return method in {'GET', 'HEAD', 'PUT', 'DELETE'}


if __name__ == '__main__':
    print(should_retry(503, 'GET'))
    print(should_retry(503, 'POST'))
