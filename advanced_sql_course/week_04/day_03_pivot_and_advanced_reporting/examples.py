# Pivot-like отчёты и advanced reporting
import sqlite3


def build_demo_db() -> sqlite3.Connection:
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row
    conn.executescript("""
    CREATE TABLE defects (id INTEGER PRIMARY KEY, team TEXT NOT NULL, severity TEXT NOT NULL);
    INSERT INTO defects VALUES (1, 'web', 'critical'), (2, 'web', 'major'), (3, 'api', 'major'), (4, 'api', 'major'), (5, 'mobile', 'minor');
    """)
    return conn


def fetch_all(conn: sqlite3.Connection, query: str):
    return [dict(row) for row in conn.execute(query).fetchall()]


def main() -> None:
    conn = build_demo_db()
    print(fetch_all(conn, """
        SELECT team,
               SUM(CASE WHEN severity = 'critical' THEN 1 ELSE 0 END) AS critical_count,
               SUM(CASE WHEN severity = 'major' THEN 1 ELSE 0 END) AS major_count,
               SUM(CASE WHEN severity = 'minor' THEN 1 ELSE 0 END) AS minor_count
        FROM defects
        GROUP BY team
        ORDER BY team
    """))


if __name__ == '__main__':
    main()
