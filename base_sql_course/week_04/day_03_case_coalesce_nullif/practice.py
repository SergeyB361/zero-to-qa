# CASE, COALESCE, NULLIF
import sqlite3


def build_demo_db() -> sqlite3.Connection:
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row
    conn.executescript("""
    CREATE TABLE defects (id INTEGER PRIMARY KEY, title TEXT NOT NULL, severity TEXT NOT NULL, owner TEXT, resolved_hours INTEGER NOT NULL);
    INSERT INTO defects VALUES
        (1, 'Login 500', 'critical', 'Boris', 4),
        (2, 'Wrong total', 'major', NULL, 0),
        (3, 'Slow export', 'minor', 'Anna', 12);
    """)
    return conn


def severity_labels(conn: sqlite3.Connection):
    return []


def owner_or_unassigned(conn: sqlite3.Connection):
    return []


def normalized_resolution_hours(conn: sqlite3.Connection):
    return []


def main() -> None:
    conn = build_demo_db()
    print('severity_labels ->', severity_labels(conn), '| expected:', "['Login 500:hot', 'Wrong total:hot', 'Slow export:normal']")
    print('owner_or_unassigned ->', owner_or_unassigned(conn), '| expected:', "['Boris', 'unassigned', 'Anna']")
    print('normalized_resolution_hours ->', normalized_resolution_hours(conn), '| expected:', '[4, None, 12]')


if __name__ == '__main__':
    main()
