import os

# День 4 — Практика: config и secrets

def load_settings() -> dict[str, str | None]:
    return {
        'base_url': None,
        'token': None,
    }


def build_headers(token: str | None) -> dict[str, str]:
    return {}


def run_checks() -> list[tuple[str, bool]]:
    os.environ['API_BASE_URL'] = 'https://stage.example.com'
    os.environ['API_TOKEN'] = 'secret-token'
    settings = load_settings()
    headers = build_headers(settings['token'])
    return [
        ('base url loaded', settings['base_url'] == 'https://stage.example.com'),
        ('token loaded', settings['token'] == 'secret-token'),
        ('auth header built', headers == {'Authorization': 'Bearer secret-token'}),
    ]


if __name__ == '__main__':
    print('Собери config loader и auth headers:')
    for name, status in run_checks():
        print(f'{name}: {status}')
