import os
from dataclasses import dataclass

from sqlalchemy import create_engine, text
from sqlalchemy.engine import make_url


@dataclass(slots=True)
class DatabaseSettings:
    database_url: str
    echo_sql: bool = False
    pool_pre_ping: bool = True

    @classmethod
    def from_env(cls) -> 'DatabaseSettings':
        return cls(
            database_url=os.environ['DATABASE_URL'],
            echo_sql=os.environ.get('ECHO_SQL', '0') == '1',
        )


def describe_target(database_url: str) -> dict[str, object | None]:
    url = make_url(database_url)
    return {
        'driver': url.drivername,
        'host': url.host,
        'port': url.port,
        'database': url.database,
    }


def build_engine_options(settings: DatabaseSettings) -> dict[str, object]:
    options: dict[str, object] = {'future': True, 'echo': settings.echo_sql}
    if settings.database_url.startswith('postgresql'):
        options['pool_pre_ping'] = settings.pool_pre_ping
    elif settings.database_url.startswith('sqlite'):
        options['connect_args'] = {'check_same_thread': False}
    return options


def run_healthcheck_sqlite() -> int:
    engine = create_engine('sqlite+pysqlite:///:memory:', future=True)
    try:
        with engine.connect() as connection:
            return connection.execute(text('SELECT 1')).scalar_one()
    finally:
        engine.dispose()


if __name__ == '__main__':
    os.environ['DATABASE_URL'] = 'postgresql+psycopg://app:secret@db:5432/appdb'
    postgres_settings = DatabaseSettings.from_env()
    print('POSTGRES TARGET ->', describe_target(postgres_settings.database_url))
    print('POSTGRES OPTIONS ->', build_engine_options(postgres_settings))

    sqlite_settings = DatabaseSettings(database_url='sqlite+pysqlite:///./local.db')
    print('SQLITE TARGET ->', describe_target(sqlite_settings.database_url))
    print('SQLITE OPTIONS ->', build_engine_options(sqlite_settings))
    print('HEALTHCHECK ->', run_healthcheck_sqlite())
