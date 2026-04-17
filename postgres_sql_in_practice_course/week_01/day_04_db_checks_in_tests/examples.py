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


def row_exists(conn: psycopg.Connection, query: str) -> bool:
    with conn.cursor() as cur:
        cur.execute(_normalize_query(query))
        return cur.fetchone() is not None


def count_rows(conn: psycopg.Connection, query: str) -> int:
    wrapped = f"SELECT COUNT(*) FROM ({_normalize_query(query)}) AS subq"
    with conn.cursor() as cur:
        cur.execute(wrapped)
        row = cur.fetchone()
    return int(row[0])


def get_scalar(conn: psycopg.Connection, query: str):
    with conn.cursor() as cur:
        cur.execute(_normalize_query(query))
        row = cur.fetchone()
    return None if row is None else row[0]


def main() -> None:
    with psycopg.connect(**get_connection_kwargs()) as conn:
        assert row_exists(
            conn,
            "SELECT 1 FROM defects WHERE severity = 'critical' AND status = 'open' LIMIT 1;",
        ) is True
        assert count_rows(
            conn,
            "SELECT id FROM tasks WHERE status <> 'closed';",
        ) == 3
        assert get_scalar(
            conn,
            "SELECT COUNT(*) FROM test_runs WHERE status = 'failed';",
        ) == 1
    print('Real DB-check example passed against zero_to_qa')


if __name__ == '__main__':
    main()
