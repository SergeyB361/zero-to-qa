from __future__ import annotations

import os
from typing import Any

import psycopg
from psycopg.rows import dict_row


def get_connection_kwargs() -> dict[str, Any]:
    return {
        'host': os.getenv('PGHOST', 'localhost'),
        'port': int(os.getenv('PGPORT', '5432')),
        'dbname': os.getenv('PGDATABASE', 'zero_to_qa'),
        'user': os.getenv('PGUSER', 'postgres'),
        'password': os.getenv('PGPASSWORD', 'postgres'),
    }


def summarize_endpoint_metrics(rows: list[dict]) -> list[str]:
    return [f"{row['endpoint']} -> {row['avg_latency_ms']}ms" for row in rows]


def main() -> None:
    with psycopg.connect(**get_connection_kwargs(), row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TEMP TABLE api_request_log (
                    release_tag TEXT,
                    endpoint TEXT,
                    status_code INTEGER,
                    latency_ms INTEGER
                )
                """
            )
            cur.executemany(
                """
                INSERT INTO api_request_log (release_tag, endpoint, status_code, latency_ms)
                VALUES (%s, %s, %s, %s)
                """,
                [
                    ('2026.04.10', '/orders', 200, 240),
                    ('2026.04.10', '/orders', 500, 480),
                    ('2026.04.10', '/login', 200, 120),
                    ('2026.04.11', '/orders', 200, 260),
                    ('2026.04.11', '/orders', 503, 520),
                    ('2026.04.11', '/profile', 200, 160),
                ],
            )
            cur.execute(
                """
                SELECT endpoint, AVG(latency_ms)::int AS avg_latency_ms
                FROM api_request_log
                GROUP BY endpoint
                ORDER BY avg_latency_ms DESC, endpoint
                """
            )
            latency_rows = cur.fetchall()
            summaries = summarize_endpoint_metrics(latency_rows)
            assert summaries[0].startswith('/orders')

            cur.execute(
                """
                SELECT
                    release_tag,
                    COUNT(*) FILTER (WHERE status_code >= 400) AS error_count
                FROM api_request_log
                GROUP BY release_tag
                ORDER BY release_tag
                """
            )
            errors_by_release = {row['release_tag']: row['error_count'] for row in cur.fetchall()}
            assert errors_by_release == {'2026.04.10': 1, '2026.04.11': 1}

    print('Real backend/API analysis example passed against Postgres')


if __name__ == '__main__':
    main()
