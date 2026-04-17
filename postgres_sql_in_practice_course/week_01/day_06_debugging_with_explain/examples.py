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
        cur.execute(f"EXPLAIN {normalized}")
        return [row[0] for row in cur.fetchall()]


def summarize_plan_findings(lines: list[str]) -> list[str]:
    findings = []
    joined = ' '.join(lines).lower()
    if 'seq scan' in joined:
        findings.append('full scan detected')
    if 'index scan' in joined or 'bitmap index scan' in joined:
        findings.append('index usage detected')
    return findings


def main() -> None:
    with psycopg.connect(**get_connection_kwargs()) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TEMP TABLE explain_demo AS
                SELECT
                    gs AS id,
                    CASE WHEN gs % 10 = 0 THEN 'failed' ELSE 'passed' END AS status
                FROM generate_series(1, 20000) AS gs
                """
            )

        plan_before = run_explain(conn, "SELECT * FROM explain_demo WHERE status = 'failed';")
        assert 'full scan detected' in summarize_plan_findings(plan_before)

        with conn.cursor() as cur:
            cur.execute("CREATE INDEX idx_explain_demo_status ON explain_demo(status)")

        plan_after = run_explain(conn, "SELECT * FROM explain_demo WHERE status = 'failed';")
        assert 'index usage detected' in summarize_plan_findings(plan_after)

    print('Real EXPLAIN debugging example passed against Postgres')


if __name__ == '__main__':
    main()
