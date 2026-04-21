"""
Практическое задание:
1. Создай `engine` из `DATABASE_URL`.
2. Создай `Session` и выполни простой ping-запрос.
3. Верни осмысленный результат из `run_probe()`.

Например:
- dialect -> `postgresql`
- probe -> `{'dialect': 'postgresql', 'ping': 1}`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

import os

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+psycopg://postgres:postgres@localhost:5432/zero_to_qa')


def run_probe() -> dict[str, object]:
    # TODO: собери real probe через engine/session.
    return {'dialect': 'TODO', 'ping': 0}


def run_checks() -> None:
    probe = run_probe()
    assert probe['dialect'] == 'postgresql', 'dialect should come from live Postgres engine'
    assert probe['ping'] == 1, 'ping query should return 1'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
