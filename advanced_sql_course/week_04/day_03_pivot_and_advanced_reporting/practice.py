# Pivot-like отчёты и advanced reporting
import sqlite3


def build_demo_db() -> sqlite3.Connection:
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row
    conn.executescript("""
    CREATE TABLE test_runs (id INTEGER PRIMARY KEY, release_tag TEXT NOT NULL, status TEXT NOT NULL);
    INSERT INTO test_runs VALUES (1, 'build-101', 'passed'), (2, 'build-101', 'failed'), (3, 'build-101', 'failed'), (4, 'build-102', 'passed'), (5, 'build-102', 'skipped'), (6, 'build-103', 'passed');
    """)
    return conn


def release_status_matrix(conn: sqlite3.Connection):
    return []


def main() -> None:
    conn = build_demo_db()
    print('release_status_matrix ->', release_status_matrix(conn), '| expected:', "['build-101:1:2:0', 'build-102:1:0:1', 'build-103:1:0:0']")


if __name__ == '__main__':
    main()
