"""
Практическое задание:
1. Отредактируй `docker-compose.practice.yml` как реальный compose-артефакт.
2. Для `app` задай корректный `DATABASE_URL` через имя сервиса `db`.
3. Для `db` добавь healthcheck и condition `service_healthy`.

Например:
- `DATABASE_URL=postgresql+psycopg://app:secret@db:5432/appdb`
- `postgres_data:/var/lib/postgresql/data`
- `depends_on.db.condition = service_healthy`
- `pg_isready -U app -d appdb`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

from pathlib import Path


DAY_DIR = Path(__file__).resolve().parent
PRACTICE_FILE = DAY_DIR / 'docker-compose.practice.yml'


def run_checks() -> None:
    content = PRACTICE_FILE.read_text(encoding='utf-8')
    assert 'TODO' not in content, 'compose practice file still contains TODO markers'
    assert 'services:' in content, 'compose file should declare services'
    assert '\n  app:\n' in content, 'compose file should include app service'
    assert '\n  db:\n' in content, 'compose file should include db service'
    assert 'DATABASE_URL: postgresql+psycopg://app:secret@db:5432/appdb' in content, 'app DATABASE_URL is incorrect'
    assert 'postgres_data:/var/lib/postgresql/data' in content, 'db service should mount postgres_data volume'
    assert 'condition: service_healthy' in content, 'app should depend on healthy db service'
    assert 'pg_isready -U app -d appdb' in content, 'db healthcheck should use pg_isready'
    assert 'volumes:' in content and 'postgres_data:' in content, 'compose runtime should define postgres_data volume'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
