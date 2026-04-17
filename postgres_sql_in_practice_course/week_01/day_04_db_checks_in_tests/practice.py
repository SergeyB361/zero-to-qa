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


def _normalize_query(query: str) -> str:
    return query.strip().rstrip(';').strip()


# Задание 1: row_exists
# Реализуй helper: есть ли строка по query.
def row_exists(conn: psycopg.Connection, query: str) -> bool:
    with conn.cursor() as cur:
        cur.execute(_normalize_query(query))
        return cur.fetchone() is not None


# Задание 2: count_rows
# Реализуй helper: количество строк в подзапросе.
def count_rows(conn: psycopg.Connection, query: str) -> int:
    wrapped = f"SELECT COUNT(*) FROM ({_normalize_query(query)}) AS subq"
    with conn.cursor() as cur:
        cur.execute(wrapped)
        return int(cur.fetchone()[0])


# Задание 3: get_scalar
# Возьми первое значение из первой строки.
def get_scalar(conn: psycopg.Connection, query: str):
    with conn.cursor() as cur:
        cur.execute(_normalize_query(query))
        row = cur.fetchone()
    return None if row is None else row[0]


# Задание 4: assert_task_created
# Проверь, что есть строка со status=open.
def assert_task_created(conn: psycopg.Connection) -> None:
    assert row_exists(conn, "SELECT 1 FROM tasks WHERE status = 'open' LIMIT 1") is True


# Задание 5: explain_when_db_check_is_justified
# Верни 3 тезиса, когда DB-check оправдан.
def explain_when_db_check_is_justified() -> list[str]:
    return [
        'когда база является источником истины для статуса или факта создания записи',
        'когда UI или API не дают надёжного способа проверить внутренний результат',
        'когда запрос проверяет конкретное бизнес-правило, а не всю базу целиком',
    ]


def run_checks() -> None:
    with psycopg.connect(**get_connection_kwargs()) as conn:
        assert row_exists(
            conn,
            "SELECT 1 FROM defects WHERE severity = 'critical' AND status = 'open' LIMIT 1",
        ) is True
        assert count_rows(conn, "SELECT id FROM tasks WHERE status <> 'closed'") == 3
        assert get_scalar(conn, "SELECT COUNT(*) FROM test_runs WHERE status = 'failed'") == 1
        assert_task_created(conn)
    assert len(explain_when_db_check_is_justified()) == 3
    print('Live DB-check practice passed.')


if __name__ == '__main__':
    run_checks()
