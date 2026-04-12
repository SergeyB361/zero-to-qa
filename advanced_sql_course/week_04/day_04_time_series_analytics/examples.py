# Time-series analytics и bucketization
import sqlite3


def build_demo_db() -> sqlite3.Connection:
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row
    conn.executescript("""
    CREATE TABLE api_checks (id INTEGER PRIMARY KEY, endpoint TEXT NOT NULL, latency_ms INTEGER NOT NULL, created_at TEXT NOT NULL);
    INSERT INTO api_checks VALUES (1, '/login', 120, '2026-04-01 10:00:00'), (2, '/login', 110, '2026-04-01 12:00:00'), (3, '/orders', 220, '2026-04-02 09:00:00'), (4, '/orders', 180, '2026-04-02 11:00:00');
    """)
    return conn


def fetch_all(conn: sqlite3.Connection, query: str):
    return [dict(row) for row in conn.execute(query).fetchall()]


def main() -> None:
    conn = build_demo_db()
    print(fetch_all(conn, "SELECT date(created_at) AS day, ROUND(AVG(latency_ms), 2) AS avg_latency FROM api_checks GROUP BY date(created_at) ORDER BY day"))


if __name__ == '__main__':
    main()
