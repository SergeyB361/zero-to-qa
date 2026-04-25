import os
from dataclasses import dataclass


TRUE_VALUES = {'1', 'true', 'yes', 'on'}


def parse_bool(raw: str | None, *, default: bool = False) -> bool:
    if raw is None:
        return default
    return raw.strip().lower() in TRUE_VALUES


@dataclass(slots=True)
class AppSettings:
    app_name: str
    debug: bool
    api_prefix: str
    page_size: int
    database_url: str

    @classmethod
    def from_env(cls) -> 'AppSettings':
        return cls(
            app_name=os.getenv('APP_NAME', 'Backend Patterns Demo'),
            debug=parse_bool(os.getenv('DEBUG')),
            api_prefix=os.getenv('API_PREFIX', '/api/v1'),
            page_size=int(os.getenv('PAGE_SIZE', '20')),
            database_url=os.getenv('DATABASE_URL', 'postgresql+psycopg://postgres:postgres@localhost:5432/app'),
        )


if __name__ == '__main__':
    os.environ['APP_NAME'] = 'Inventory API'
    os.environ['DEBUG'] = 'true'
    os.environ['API_PREFIX'] = '/api/internal'
    os.environ['PAGE_SIZE'] = '50'
    os.environ['DATABASE_URL'] = 'postgresql+psycopg://postgres:postgres@localhost:5432/inventory'

    settings = AppSettings.from_env()
    print(settings)
    print('debug ->', settings.debug)
    print('page_size ->', settings.page_size)
