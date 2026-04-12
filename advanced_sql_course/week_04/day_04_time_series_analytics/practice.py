# Time-series analytics и bucketization
import sqlite3


def build_demo_db() -> sqlite3.Connection:
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row
    conn.executescript("""
    CREATE TABLE api_checks (id INTEGER PRIMARY KEY, endpoint TEXT NOT NULL, latency_ms INTEGER NOT NULL, status_code INTEGER NOT NULL, created_at TEXT NOT NULL);
    INSERT INTO api_checks VALUES (1, '/login', 120, 200, '2026-04-01 10:00:00'), (2, '/login', 90, 401, '2026-04-01 12:00:00'), (3, '/orders', 220, 200, '2026-04-02 09:00:00'), (4, '/orders', 180, 500, '2026-04-02 11:00:00'), (5, '/reports', 450, 200, '2026-04-03 08:00:00');
    """)
    return conn


def avg_latency_per_day(conn: sqlite3.Connection):
    return []


def failing_checks_per_day(conn: sqlite3.Connection):
    return []


def main() -> None:
    conn = build_demo_db()
    print('avg_latency_per_day ->', avg_latency_per_day(conn), '| expected:', "['2026-04-01:105.0', '2026-04-02:200.0', '2026-04-03:450.0']")
    print('failing_checks_per_day ->', failing_checks_per_day(conn), '| expected:', "['2026-04-01:1', '2026-04-02:1']")


if __name__ == '__main__':
    main()
