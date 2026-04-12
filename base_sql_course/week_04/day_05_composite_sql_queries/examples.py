# Композитные SQL-запросы
import sqlite3


def build_demo_db() -> sqlite3.Connection:
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row
    conn.executescript("""
    CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL, team TEXT NOT NULL);
    CREATE TABLE tasks (id INTEGER PRIMARY KEY, assignee_id INTEGER NOT NULL, status TEXT NOT NULL, priority TEXT NOT NULL, estimate_hours INTEGER NOT NULL, FOREIGN KEY(assignee_id) REFERENCES users(id));
    INSERT INTO users VALUES (1, 'Anna', 'web'), (2, 'Boris', 'api'), (3, 'Nina', 'mobile');
    INSERT INTO tasks VALUES
        (1, 1, 'open', 'high', 5),
        (2, 1, 'closed', 'low', 2),
        (3, 2, 'open', 'high', 8),
        (4, 2, 'open', 'medium', 3),
        (5, 3, 'open', 'medium', 6);
    """)
    return conn


def fetch_all(conn: sqlite3.Connection, query: str):
    return [dict(row) for row in conn.execute(query).fetchall()]


def main() -> None:
    conn = build_demo_db()
    print(fetch_all(conn, """
        SELECT u.team, COUNT(*) AS open_tasks, SUM(t.estimate_hours) AS total_estimate
        FROM tasks AS t
        INNER JOIN users AS u ON t.assignee_id = u.id
        WHERE t.status = 'open'
        GROUP BY u.team
        ORDER BY total_estimate DESC
    """))


if __name__ == '__main__':
    main()
