"""
Практическое задание:
1. Собери настройки сервиса в одном объекте.
2. Прочитай значения из env и преобразуй типы.
3. Дай разумные defaults, если env не задан.

Например:
- `APP_NAME=Orders API`
- `DEBUG=true`
- `PAGE_SIZE=100`
- `API_PREFIX=/api/internal`

Ожидается, что итоговый объект настроек вернёт:
- `app_name == 'Orders API'`
- `debug is True`
- `page_size == 100`
- `api_prefix == '/api/internal'`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

import os
from dataclasses import dataclass


TRUE_VALUES = {'1', 'true', 'yes', 'on'}


def parse_bool(raw: str | None, *, default: bool = False) -> bool:
    if raw is None:
        return default
    # TODO: преобразовать строку в bool через TRUE_VALUES.
    return False


@dataclass(slots=True)
class ServiceSettings:
    app_name: str
    debug: bool
    api_prefix: str
    page_size: int
    database_url: str

    @classmethod
    def from_env(cls) -> 'ServiceSettings':
        # TODO: прочитать env и вернуть корректный объект настроек.
        return cls(
            app_name='TODO',
            debug=False,
            api_prefix='/todo',
            page_size=0,
            database_url='TODO',
        )


def run_checks() -> None:
    snapshot = dict(os.environ)
    try:
        os.environ['APP_NAME'] = 'Orders API'
        os.environ['DEBUG'] = 'true'
        os.environ['API_PREFIX'] = '/api/internal'
        os.environ['PAGE_SIZE'] = '100'
        os.environ['DATABASE_URL'] = 'postgresql+psycopg://postgres:postgres@localhost:5432/orders'

        settings = ServiceSettings.from_env()
        assert settings.app_name == 'Orders API', 'app_name should come from APP_NAME env'
        assert settings.debug is True, 'DEBUG=true should become True'
        assert settings.api_prefix == '/api/internal', 'API prefix should come from env'
        assert settings.page_size == 100, 'PAGE_SIZE should be parsed as int'
        assert settings.database_url.endswith('/orders'), 'DATABASE_URL should come from env'

        for key in ['APP_NAME', 'DEBUG', 'API_PREFIX', 'PAGE_SIZE', 'DATABASE_URL']:
            os.environ.pop(key, None)

        fallback = ServiceSettings.from_env()
        assert fallback.app_name == 'Backend Service', 'fallback app_name should be Backend Service'
        assert fallback.debug is False, 'fallback debug should be False'
        assert fallback.api_prefix == '/api/v1', 'fallback prefix should be /api/v1'
        assert fallback.page_size == 20, 'fallback page size should be 20'
    finally:
        os.environ.clear()
        os.environ.update(snapshot)


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
