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


def run_explain(conn: psycopg.Connection, query: str) -> list[str]:
    normalized = query.strip().rstrip(';').strip()
    with conn.cursor() as cur:
        cur.execute(f'EXPLAIN {normalized}')
        return [row[0] for row in cur.fetchall()]


# Задание 1: detect_seq_scan
# Если в плане есть Seq Scan, верни True.
def detect_seq_scan(lines: list[str]) -> bool:
    return 'seq scan' in ' '.join(lines).lower()


# Задание 2: detect_index_usage
# Если в плане есть Index Scan или Bitmap Index Scan, верни True.
def detect_index_usage(lines: list[str]) -> bool:
    joined = ' '.join(lines).lower()
    return 'index scan' in joined or 'bitmap index scan' in joined


# Задание 3: explain_findings_summary
# Верни список коротких выводов по плану.
def explain_findings_summary(lines: list[str]) -> list[str]:
    findings = []
    if detect_seq_scan(lines):
        findings.append('full scan detected')
    if detect_index_usage(lines):
        findings.append('index usage detected')
    return findings


# Задание 4: write_debugging_workflow
# Верни 4 шага EXPLAIN-debugging workflow.
def write_debugging_workflow() -> list[str]:
    return [
        'взять конкретный медленный или подозрительный запрос',
        'снять baseline plan через EXPLAIN',
        'попробовать индекс или rewrite и снять plan повторно',
        'сформулировать краткий вывод по изменению плана',
    ]


# Задание 5: explain_when_to_use_analyze
# Верни 2-3 тезиса, когда нужен EXPLAIN ANALYZE.
def explain_when_to_use_analyze() -> list[str]:
    return [
        'когда нужно увидеть реальные timing и row counts, а не только оценку planner',
        'когда baseline EXPLAIN не объясняет, где именно тратится время',
        'когда запрос безопасно запускать и его выполнение не повредит данным',
    ]


def run_checks() -> None:
    assert len(write_debugging_workflow()) == 4
    assert 2 <= len(explain_when_to_use_analyze()) <= 3

    with psycopg.connect(**get_connection_kwargs()) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TEMP TABLE explain_practice_demo AS
                SELECT
                    gs AS id,
                    CASE WHEN gs % 10 = 0 THEN 'failed' ELSE 'passed' END AS status
                FROM generate_series(1, 20000) AS gs
                """
            )
        plan_before = run_explain(conn, "SELECT * FROM explain_practice_demo WHERE status = 'failed'")
        assert detect_seq_scan(plan_before) is True
        assert explain_findings_summary(plan_before) == ['full scan detected']

        with conn.cursor() as cur:
            cur.execute('CREATE INDEX idx_explain_practice_demo_status ON explain_practice_demo(status)')
        plan_after = run_explain(conn, "SELECT * FROM explain_practice_demo WHERE status = 'failed'")
        assert detect_index_usage(plan_after) is True
        assert 'index usage detected' in explain_findings_summary(plan_after)

    print('EXPLAIN practice checks passed.')


if __name__ == '__main__':
    run_checks()
