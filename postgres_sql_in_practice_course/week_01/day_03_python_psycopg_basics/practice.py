from __future__ import annotations

import os
from typing import Any


def get_connection_kwargs() -> dict[str, Any]:
    return {
        'host': os.getenv('PGHOST', 'localhost'),
        'port': int(os.getenv('PGPORT', '5432')),
        'dbname': os.getenv('PGDATABASE', 'zero_to_qa'),
        'user': os.getenv('PGUSER', 'postgres'),
        'password': os.getenv('PGPASSWORD', 'postgres'),
    }


# Задание 1: fetch_users_count
# Верни количество пользователей.
def fetch_users_count() -> int:
    return -1


# Задание 2: fetch_project_names
# Верни список имён проектов.
def fetch_project_names() -> list[str]:
    return []


# Задание 3: fetch_open_task_ids
# Верни id задач со статусом open.
def fetch_open_task_ids() -> list[int]:
    return []


# Задание 4: fetch_failed_runs_count
# Верни количество failed test_runs.
def fetch_failed_runs_count() -> int:
    return -1


# Задание 5: explain_connection_flow
# Верни 3 коротких тезиса про connect/cursor/close.
def explain_connection_flow() -> list[str]:
    return ['TODO']


def run_checks() -> None:
    assert isinstance(explain_connection_flow(), list)
    print('Scaffold checks passed. Для live-run нужен psycopg.')


if __name__ == '__main__':
    run_checks()
