"""
Практическое задание:
1. Реализуй разбор database target из URL.
2. Собери engine options отдельно для `Postgres` и `SQLite`.
3. Верни health check SQL так, чтобы runtime мог явно проверить доступность БД.

Например:
- `postgresql+psycopg://app:secret@db:5432/appdb` -> `{'driver': 'postgresql+psycopg', 'host': 'db', 'port': 5432, 'database': 'appdb'}`
- options для Postgres -> `{'future': True, 'echo': False, 'pool_pre_ping': True}`
- options для SQLite -> `{'future': True, 'echo': False, 'connect_args': {'check_same_thread': False}}`
- health check SQL -> `SELECT 1`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

from dataclasses import dataclass

from sqlalchemy import create_engine, text
from sqlalchemy.engine import make_url


@dataclass(slots=True)
class DatabaseSettings:
    database_url: str
    echo_sql: bool = False
    pool_pre_ping: bool = True


def describe_target(database_url: str) -> dict[str, object | None]:
    # TODO: разобрать URL через make_url и вернуть driver/host/port/database.
    return {'driver': 'TODO', 'host': None, 'port': None, 'database': 'TODO'}


def build_engine_options(settings: DatabaseSettings) -> dict[str, object]:
    # TODO: для Postgres вернуть future/echo/pool_pre_ping, для SQLite вернуть future/echo/connect_args.
    return {'future': True}


def healthcheck_sql() -> str:
    # TODO: вернуть минимальный SQL для проверки доступности БД.
    return 'TODO'


def run_checks() -> None:
    postgres = DatabaseSettings(database_url='postgresql+psycopg://app:secret@db:5432/appdb')
    sqlite = DatabaseSettings(database_url='sqlite+pysqlite:///./local.db')

    assert describe_target(postgres.database_url) == {
        'driver': 'postgresql+psycopg',
        'host': 'db',
        'port': 5432,
        'database': 'appdb',
    }, 'postgres target description is incorrect'

    assert build_engine_options(postgres) == {
        'future': True,
        'echo': False,
        'pool_pre_ping': True,
    }, 'postgres engine options are incorrect'

    assert build_engine_options(sqlite) == {
        'future': True,
        'echo': False,
        'connect_args': {'check_same_thread': False},
    }, 'sqlite engine options are incorrect'

    assert healthcheck_sql() == 'SELECT 1', 'healthcheck SQL should be SELECT 1'

    engine = create_engine('sqlite+pysqlite:///:memory:', future=True)
    try:
        with engine.connect() as connection:
            assert connection.execute(text(healthcheck_sql())).scalar_one() == 1, 'healthcheck SQL should execute successfully'
    finally:
        engine.dispose()


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
