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


def collect_context() -> dict:
    with psycopg.connect(**get_connection_kwargs()) as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT COUNT(*) FROM tasks')
            tasks_count = cur.fetchone()[0]
            cur.execute('SELECT COUNT(*) FROM defects')
            defects_count = cur.fetchone()[0]
            cur.execute(
                """
                SELECT COUNT(*)
                FROM defects
                WHERE status IN ('open', 'in_progress')
                """
            )
            active_defects = cur.fetchone()[0]
    return {
        'tasks_count': int(tasks_count),
        'defects_count': int(defects_count),
        'active_defects': int(active_defects),
    }


# core queries should return a compact investigation snapshot
def run_core_queries() -> list[dict]:
    with psycopg.connect(**get_connection_kwargs(), row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT
                    'open_critical_defects' AS check_name,
                    COUNT(*)::int AS check_value
                FROM defects
                WHERE severity = 'critical'
                  AND status IN ('open', 'in_progress')
                UNION ALL
                SELECT
                    'blocked_tasks' AS check_name,
                    COUNT(*)::int AS check_value
                FROM tasks
                WHERE status = 'blocked'
                UNION ALL
                SELECT
                    'closed_tasks_with_active_defects' AS check_name,
                    COUNT(*)::int AS check_value
                FROM tasks t
                JOIN defects d ON d.task_id = t.id
                WHERE t.status = 'closed'
                  AND d.status IN ('open', 'in_progress')
                ORDER BY check_name
                """
            )
            return cur.fetchall()


# summarize findings for another engineer
def summarize_findings(rows: list[dict]) -> list[str]:
    return [f"{row['check_name']}: {row['check_value']}" for row in rows]


def main() -> None:
    context = collect_context()
    rows = run_core_queries()
    findings = summarize_findings(rows)

    assert context['tasks_count'] == 4
    assert context['defects_count'] == 3
    assert context['active_defects'] == 2
    assert 'open_critical_defects: 2' in findings
    assert 'blocked_tasks: 1' in findings
    assert 'closed_tasks_with_active_defects: 1' in findings

    print(context)
    for finding in findings:
        print(finding)


if __name__ == '__main__':
    main()
