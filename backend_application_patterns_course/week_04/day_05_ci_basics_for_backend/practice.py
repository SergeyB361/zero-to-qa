"""
Практическое задание:
1. Отредактируй `backend-ci.practice.yml` как реальный CI workflow.
2. Включи install, compile/lint-like step, tests и migration sanity.
3. Сохрани порядок, который даёт быстрый и понятный сигнал.

Например:
- checkout
- setup python
- install dependencies
- compile or lint
- tests
- migration sanity

Критерий готовности: `run_checks()` проходит без ошибок.
"""

from pathlib import Path


DAY_DIR = Path(__file__).resolve().parent
WORKFLOW_FILE = DAY_DIR / 'backend-ci.practice.yml'


def run_checks() -> None:
    content = WORKFLOW_FILE.read_text(encoding='utf-8')
    assert 'TODO' not in content, 'CI practice file still contains TODO markers'

    expected_steps = [
        'actions/checkout@v4',
        'actions/setup-python@v5',
        'python -m pip install -r requirements.txt',
        'python -m compileall app tests',
        'pytest -q',
        'alembic upgrade head',
    ]

    last_index = -1
    for step in expected_steps:
        index = content.find(step)
        assert index != -1, f'workflow is missing required step: {step}'
        assert index > last_index, f'workflow step order is incorrect around: {step}'
        last_index = index


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
