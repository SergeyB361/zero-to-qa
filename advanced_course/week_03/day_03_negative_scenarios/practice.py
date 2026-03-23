# День 3 — Практика: negative scenarios

def validate_user_payload(payload: dict[str, object]) -> tuple[int, str]:
    if 'email' not in payload:
        return 400, 'email is required'
    if not isinstance(payload.get('age'), int):
        return 400, 'age must be int'
    if payload.get('status') not in {'new', 'active', 'blocked'}:
        return 400, 'invalid status'
    return 201, 'created'


def describe_negative_cases() -> list[str]:
    return []


def run_checks() -> list[tuple[str, bool]]:
    cases_text = ' '.join(describe_negative_cases()).lower()
    return [
        ('missing field fails', validate_user_payload({'age': 18, 'status': 'new'})[0] == 400),
        ('wrong type fails', validate_user_payload({'email': 'qa@example.com', 'age': '18', 'status': 'new'})[0] == 400),
        ('invalid enum fails', validate_user_payload({'email': 'qa@example.com', 'age': 18, 'status': 'unknown'})[0] == 400),
        ('negative cases mention missing field', 'missing' in cases_text or 'required' in cases_text),
        ('negative cases mention wrong type', 'type' in cases_text or 'int' in cases_text),
        ('negative cases mention auth or forbidden', '401' in cases_text or '403' in cases_text or 'forbidden' in cases_text),
    ]


if __name__ == '__main__':
    print('Опиши негативные сценарии и проверь базовый валидатор:')
    for name, status in run_checks():
        print(f'{name}: {status}')
