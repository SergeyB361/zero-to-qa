from pathlib import Path


DAY_DIR = Path(__file__).resolve().parent
COMPOSE_EXAMPLE = DAY_DIR / 'docker-compose.example.yml'


if __name__ == '__main__':
    content = COMPOSE_EXAMPLE.read_text(encoding='utf-8')
    print(content)
    print('HAS APP SERVICE ->', 'app:' in content)
    print('HAS DB SERVICE ->', 'db:' in content)
    print('HAS DATABASE_URL ->', 'postgresql+psycopg://app:secret@db:5432/appdb' in content)
