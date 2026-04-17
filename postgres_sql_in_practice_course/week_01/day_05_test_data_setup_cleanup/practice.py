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


# Задание 1: build_test_task_payload
# Собери словарь для тестовой задачи.
def build_test_task_payload(task_id: int) -> dict:
    return {
        'task_id': task_id,
        'status': 'open',
        'priority': 'low',
        'estimate_points': 1,
    }


# Задание 2: collect_created_ids
# Верни список id, которые надо потом удалить.
def collect_created_ids(*ids: int) -> list[int]:
    return sorted(set(ids))


# Задание 3: cleanup_plan
# Верни 3 шага cleanup-плана.
def cleanup_plan() -> list[str]:
    return [
        'создать тестовые данные через изолированный setup-шаг',
        'зафиксировать id созданных записей во время сценария',
        'в конце удалить данные или откатить транзакцию',
    ]


# Задание 4: choose_seed_strategy
# Верни 3 тезиса: fixed seed, test-specific seed, rollback.
def choose_seed_strategy() -> list[str]:
    return [
        'fixed seed нужен для общей стабильной базы и repeatable demo-данных',
        'test-specific seed нужен, когда сценарий требует уникального набора записей',
        'rollback удобен, когда тест можно полностью обернуть в транзакцию',
    ]


# Задание 5: explain_repeatability
# Верни 2-3 тезиса, почему repeatable seed важен.
def explain_repeatability() -> list[str]:
    return [
        'одни и те же данные упрощают сравнение результатов между прогонами',
        'repeatable seed убирает случайность из SQL-проверок и расследований',
        'стабильный seed помогает быстрее локализовать регрессию',
    ]


def run_checks() -> None:
    payload = build_test_task_payload(501)
    assert payload == {
        'task_id': 501,
        'status': 'open',
        'priority': 'low',
        'estimate_points': 1,
    }
    assert collect_created_ids(3, 1, 3, 2) == [1, 2, 3]
    assert len(cleanup_plan()) == 3
    assert len(choose_seed_strategy()) == 3
    assert 2 <= len(explain_repeatability()) <= 3

    with psycopg.connect(**get_connection_kwargs()) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TEMP TABLE practice_cleanup_demo (
                    task_id INTEGER PRIMARY KEY,
                    status TEXT NOT NULL,
                    priority TEXT NOT NULL,
                    estimate_points INTEGER NOT NULL
                )
                """
            )
            cur.execute(
                """
                INSERT INTO practice_cleanup_demo (task_id, status, priority, estimate_points)
                VALUES (%s, %s, %s, %s)
                """,
                (
                    payload['task_id'],
                    payload['status'],
                    payload['priority'],
                    payload['estimate_points'],
                ),
            )
            cur.execute('SELECT COUNT(*) FROM practice_cleanup_demo')
            assert cur.fetchone()[0] == 1
            cur.execute('DELETE FROM practice_cleanup_demo WHERE task_id = %s', (payload['task_id'],))
            cur.execute('SELECT COUNT(*) FROM practice_cleanup_demo')
            assert cur.fetchone()[0] == 0

    print('Setup/cleanup practice checks passed.')


if __name__ == '__main__':
    run_checks()
