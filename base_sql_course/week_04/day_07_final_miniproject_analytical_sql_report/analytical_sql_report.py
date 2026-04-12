# Финальный мини-проект: Analytical SQL Report
import sqlite3


def build_demo_db() -> sqlite3.Connection:
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row
    conn.executescript("""
    CREATE TABLE projects (id INTEGER PRIMARY KEY, name TEXT NOT NULL);
    CREATE TABLE tasks (id INTEGER PRIMARY KEY, project_id INTEGER NOT NULL, status TEXT NOT NULL, priority TEXT NOT NULL, estimate_hours INTEGER NOT NULL, FOREIGN KEY(project_id) REFERENCES projects(id));
    CREATE TABLE test_runs (id INTEGER PRIMARY KEY, project_id INTEGER NOT NULL, status TEXT NOT NULL, executed_at TEXT NOT NULL, FOREIGN KEY(project_id) REFERENCES projects(id));
    INSERT INTO projects VALUES (1, 'Portal'), (2, 'API'), (3, 'Mobile');
    INSERT INTO tasks VALUES
        (1, 1, 'open', 'high', 5),
        (2, 1, 'closed', 'low', 2),
        (3, 2, 'open', 'high', 8),
        (4, 2, 'open', 'medium', 3),
        (5, 3, 'closed', 'low', 1);
    INSERT INTO test_runs VALUES
        (1, 1, 'passed', '2026-04-01 10:00:00'),
        (2, 1, 'failed', '2026-04-01 11:00:00'),
        (3, 2, 'passed', '2026-04-02 09:00:00'),
        (4, 2, 'failed', '2026-04-02 11:00:00');
    """)
    return conn


def project_load_report(conn: sqlite3.Connection):
    return []


def priority_mix_report(conn: sqlite3.Connection):
    return {}


def daily_run_report(conn: sqlite3.Connection):
    return []


def main() -> None:
    conn = build_demo_db()
    print('project_load_report ->', project_load_report(conn), '| expected:', "['API:2:11', 'Portal:1:5']")
    print('priority_mix_report ->', priority_mix_report(conn), '| expected:', "{'high': 2, 'medium': 1, 'low': 0}")
    print('daily_run_report ->', daily_run_report(conn), '| expected:', "['2026-04-01:2', '2026-04-02:2']")


if __name__ == '__main__':
    main()
