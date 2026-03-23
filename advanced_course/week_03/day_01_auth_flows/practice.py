# День 1 — Практика: auth flows

def auth_headers(token: str | None) -> dict[str, str]:
    if not token:
        return {}
    return {}


def classify_auth_result(status_code: int) -> str:
    return 'unexpected'


def refresh_flow_steps() -> list[str]:
    return []


def run_checks() -> list[tuple[str, bool]]:
    return [
        ('auth header present', auth_headers('valid-token') == {'Authorization': 'Bearer valid-token'}),
        ('missing token empty headers', auth_headers(None) == {}),
        ('401 classified', classify_auth_result(401) == 'unauthorized'),
        ('403 classified', classify_auth_result(403) == 'forbidden'),
        ('refresh mentions access token', 'access' in ' '.join(refresh_flow_steps()).lower()),
        ('refresh mentions refresh token', 'refresh' in ' '.join(refresh_flow_steps()).lower()),
    ]


if __name__ == '__main__':
    print('Собери базовый auth flow:')
    for name, status in run_checks():
        print(f'{name}: {status}')
