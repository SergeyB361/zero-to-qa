# Дата и время в SQL
import sqlite3


def build_demo_db() -> sqlite3.Connection:
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row
    conn.executescript("""
    CREATE TABLE api_events (id INTEGER PRIMARY KEY, endpoint TEXT NOT NULL, created_at TEXT NOT NULL);
    INSERT INTO api_events VALUES
        (1, '/login', '2026-04-01 10:00:00'),
        (2, '/orders', '2026-04-01 11:10:00'),
        (3, '/login', '2026-04-02 08:50:00'),
        (4, '/reports', '2026-04-02 09:20:00');
    """)
    return conn


def events_per_day(conn: sqlite3.Connection):
    return []


def month_buckets(conn: sqlite3.Connection):
    return []


def next_day_after_first_event(conn: sqlite3.Connection):
    return ''


def main() -> None:
    conn = build_demo_db()
    print('events_per_day ->', events_per_day(conn), '| expected:', "['2026-04-01:2', '2026-04-02:2']")
    print('month_buckets ->', month_buckets(conn), '| expected:', "['2026-04', '2026-04', '2026-04', '2026-04']")
    print('next_day_after_first_event ->', next_day_after_first_event(conn), '| expected:', '2026-04-02')


if __name__ == '__main__':
    main()
