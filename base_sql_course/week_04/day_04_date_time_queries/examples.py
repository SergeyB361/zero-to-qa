# Дата и время в SQL
import sqlite3


def build_demo_db() -> sqlite3.Connection:
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row
    conn.executescript("""
    CREATE TABLE test_runs (id INTEGER PRIMARY KEY, status TEXT NOT NULL, executed_at TEXT NOT NULL);
    INSERT INTO test_runs VALUES
        (1, 'passed', '2026-04-01 10:00:00'),
        (2, 'failed', '2026-04-01 12:15:00'),
        (3, 'passed', '2026-04-02 09:40:00');
    """)
    return conn


def fetch_all(conn: sqlite3.Connection, query: str):
    return [dict(row) for row in conn.execute(query).fetchall()]


def main() -> None:
    conn = build_demo_db()
    print(fetch_all(conn, "SELECT date(executed_at) AS day, COUNT(*) AS total FROM test_runs GROUP BY date(executed_at) ORDER BY day"))
    print(fetch_all(conn, "SELECT id, strftime('%Y-%m', executed_at) AS month_bucket FROM test_runs ORDER BY id"))


if __name__ == '__main__':
    main()
