# CASE, COALESCE, NULLIF
import sqlite3


def build_demo_db() -> sqlite3.Connection:
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row
    conn.executescript("""
    CREATE TABLE tasks (id INTEGER PRIMARY KEY, title TEXT NOT NULL, priority TEXT NOT NULL, assignee TEXT, estimate_hours INTEGER NOT NULL);
    INSERT INTO tasks VALUES
        (1, 'Login works', 'high', 'Anna', 5),
        (2, 'Refund order', 'critical', NULL, 0),
        (3, 'Export report', 'low', 'Oleg', 2);
    """)
    return conn


def fetch_all(conn: sqlite3.Connection, query: str):
    return [dict(row) for row in conn.execute(query).fetchall()]


def main() -> None:
    conn = build_demo_db()
    print(fetch_all(conn, """
        SELECT title,
               CASE WHEN priority IN ('critical', 'high') THEN 'hot' ELSE 'normal' END AS bucket,
               COALESCE(assignee, 'unassigned') AS assignee_name,
               NULLIF(estimate_hours, 0) AS normalized_estimate
        FROM tasks
        ORDER BY id
    """))


if __name__ == '__main__':
    main()
