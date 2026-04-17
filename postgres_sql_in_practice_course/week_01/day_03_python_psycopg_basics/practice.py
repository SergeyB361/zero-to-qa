from __future__ import annotations

import os
from typing import Any

import psycopg


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
    with psycopg.connect(**get_connection_kwargs()) as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT COUNT(*) FROM users')
            return int(cur.fetchone()[0])


# Задание 2: fetch_project_names
# Верни список имён проектов.
def fetch_project_names() -> list[str]:
    with psycopg.connect(**get_connection_kwargs()) as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT name FROM projects ORDER BY id')
            return [row[0] for row in cur.fetchall()]


# Задание 3: fetch_open_task_ids
# Верни id задач со статусом open.
def fetch_open_task_ids() -> list[int]:
    with psycopg.connect(**get_connection_kwargs()) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM tasks WHERE status = 'open' ORDER BY id")
            return [int(row[0]) for row in cur.fetchall()]


# Задание 4: fetch_failed_runs_count
# Верни количество failed test_runs.
def fetch_failed_runs_count() -> int:
    with psycopg.connect(**get_connection_kwargs()) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM test_runs WHERE status = 'failed'")
            return int(cur.fetchone()[0])


# Задание 5: explain_connection_flow
# Верни 3 коротких тезиса про connect/cursor/close.
def explain_connection_flow() -> list[str]:
    return [
        'connect открывает соединение с Postgres по явным параметрам окружения.',
        'cursor выполняет SQL и получает результат через fetchone/fetchall.',
        'контекстный менеджер закрывает cursor и connection без ручного close.',
    ]


def run_checks() -> None:
    assert fetch_users_count() == 4
    assert fetch_project_names() == ['Web Portal', 'Public API', 'Mobile App']
    assert fetch_open_task_ids() == [1]
    assert fetch_failed_runs_count() == 1
    assert len(explain_connection_flow()) == 3
    print('Live psycopg practice checks passed.')


if __name__ == '__main__':
    run_checks()
