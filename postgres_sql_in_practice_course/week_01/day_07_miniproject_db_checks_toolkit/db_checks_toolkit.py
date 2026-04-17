from __future__ import annotations

import os
from typing import Any

import psycopg
from psycopg import sql


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


def status_distribution(conn: psycopg.Connection, table_name: str, column_name: str) -> dict[str, int]:
    query = sql.SQL(
        """
        SELECT {column}, COUNT(*) AS cnt
        FROM {table}
        GROUP BY {column}
        ORDER BY {column}
        """
    ).format(
        column=sql.Identifier(column_name),
        table=sql.Identifier(table_name),
    )
    with conn.cursor() as cur:
        cur.execute(query)
        rows = cur.fetchall()
    return {str(status): int(count) for status, count in rows}


def main() -> None:
    with psycopg.connect(**get_connection_kwargs()) as conn:
        critical_exists = row_exists(
            conn,
            "SELECT 1 FROM defects WHERE severity = 'critical' AND status = 'open' LIMIT 1;",
        )
        open_tasks_count = count_rows(
            conn,
            "SELECT id FROM tasks WHERE status <> 'closed';",
        )
        failed_runs = get_scalar(
            conn,
            "SELECT COUNT(*) FROM test_runs WHERE status = 'failed';",
        )
        run_statuses = status_distribution(conn, 'test_runs', 'status')

        assert critical_exists is True
        assert open_tasks_count == 3
        assert failed_runs == 1
        assert run_statuses == {'blocked': 1, 'failed': 1, 'passed': 2}

        print(f'critical_exists: {critical_exists}')
        print(f'open_tasks_count: {open_tasks_count}')
        print(f'failed_runs: {failed_runs}')
        print(f'run_statuses: {run_statuses}')


if __name__ == '__main__':
    main()
