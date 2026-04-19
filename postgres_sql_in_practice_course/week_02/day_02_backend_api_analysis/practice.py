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


def seed_operational_demo(conn: psycopg.Connection) -> None:
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
        cur.execute(
            """
            CREATE TEMP TABLE release_defects (
                release_tag TEXT,
                severity TEXT,
                defect_count INTEGER
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
        cur.executemany(
            """
            INSERT INTO release_defects (release_tag, severity, defect_count)
            VALUES (%s, %s, %s)
            """,
            [
                ('2026.04.10', 'critical', 1),
                ('2026.04.10', 'major', 2),
                ('2026.04.11', 'critical', 2),
                ('2026.04.11', 'major', 1),
            ],
        )


# Задание 1: slow_endpoints
# Верни список endpoint -> avg_latency.
def slow_endpoints(conn: psycopg.Connection) -> list[str]:
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            """
            SELECT endpoint, AVG(latency_ms)::int AS avg_latency_ms
            FROM api_request_log
            GROUP BY endpoint
            ORDER BY avg_latency_ms DESC, endpoint
            """
        )
        rows = cur.fetchall()
    return [f"{row['endpoint']} -> {row['avg_latency_ms']}ms" for row in rows]


# Задание 2: error_rate_by_release
# Верни release -> error_count.
def error_rate_by_release(conn: psycopg.Connection) -> dict[str, int]:
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            """
            SELECT release_tag, COUNT(*) FILTER (WHERE status_code >= 400) AS error_count
            FROM api_request_log
            GROUP BY release_tag
            ORDER BY release_tag
            """
        )
        rows = cur.fetchall()
    return {row['release_tag']: int(row['error_count']) for row in rows}


# Задание 3: critical_defects_by_release
# Верни release -> critical defects count.
def critical_defects_by_release(conn: psycopg.Connection) -> dict[str, int]:
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            """
            SELECT release_tag, defect_count
            FROM release_defects
            WHERE severity = 'critical'
            ORDER BY release_tag
            """
        )
        rows = cur.fetchall()
    return {row['release_tag']: int(row['defect_count']) for row in rows}


# Задание 4: investigation_question_templates
# Верни 3 хороших backend investigation questions.
def investigation_question_templates() -> list[str]:
    return [
        'Какой endpoint даёт самый высокий latency после релиза?',
        'В каком релизе выросло число server-side ошибок?',
        'Есть ли связь между ростом ошибок и критическими дефектами релиза?',
    ]


# Задание 5: explain_operational_sql
# Верни 3 тезиса, чем operational SQL отличается от “учебного отчёта”.
def explain_operational_sql() -> list[str]:
    return [
        'operational SQL отвечает на конкретный инженерный вопрос, а не просто показывает красивые агрегаты',
        'в operational SQL важны скорость ответа и воспроизводимость запроса под инцидент или релиз',
        'такие запросы связывают данные с действием: что чинить, где искать проблему, как подтвердить гипотезу',
    ]


def run_checks() -> None:
    assert len(investigation_question_templates()) == 3
    assert len(explain_operational_sql()) == 3

    with psycopg.connect(**get_connection_kwargs()) as conn:
        seed_operational_demo(conn)
        assert slow_endpoints(conn) == ['/orders -> 375ms', '/profile -> 160ms', '/login -> 120ms']
        assert error_rate_by_release(conn) == {'2026.04.10': 1, '2026.04.11': 1}
        assert critical_defects_by_release(conn) == {'2026.04.10': 1, '2026.04.11': 2}

    print('Backend/API analysis practice checks passed.')


if __name__ == '__main__':
    run_checks()
