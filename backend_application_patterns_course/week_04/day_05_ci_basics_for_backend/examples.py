from pathlib import Path


DAY_DIR = Path(__file__).resolve().parent
WORKFLOW_FILE = DAY_DIR / 'backend-ci.example.yml'


if __name__ == '__main__':
    content = WORKFLOW_FILE.read_text(encoding='utf-8')
    print(content)
    print('HAS CHECKOUT ->', 'actions/checkout@v4' in content)
    print('HAS TESTS ->', 'pytest -q' in content)
    print('HAS MIGRATION SANITY ->', 'alembic upgrade head' in content)
