# День 2 — Практика: retries и idempotency

RETRYABLE_CODES = {408, 429, 500, 502, 503, 504}


def should_retry(status_code: int, method: str) -> bool:
    return False


def classify_operation(method: str, has_idempotency_key: bool) -> str:
    return 'needs-analysis'


def run_checks() -> list[tuple[str, bool]]:
    return [
        ('retry GET 503', should_retry(503, 'GET') is True),
        ('no retry POST 503', should_retry(503, 'POST') is False),
        ('no retry 400', should_retry(400, 'GET') is False),
        ('classify POST without key risky', classify_operation('POST', False) == 'risky'),
        ('classify POST with key needs-analysis', classify_operation('POST', True) == 'needs-analysis'),
        ('classify PUT safe', classify_operation('PUT', False) == 'safe'),
    ]


if __name__ == '__main__':
    print('Раздели retry policy и idempotency:')
    for name, status in run_checks():
        print(f'{name}: {status}')
