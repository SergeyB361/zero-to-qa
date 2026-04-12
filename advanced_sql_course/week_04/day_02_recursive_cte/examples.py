# Recursive CTE
import sqlite3


def build_demo_db() -> sqlite3.Connection:
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row
    conn.executescript("""
    CREATE TABLE categories (id INTEGER PRIMARY KEY, name TEXT NOT NULL, parent_id INTEGER);
    INSERT INTO categories VALUES (1, 'root', NULL), (2, 'api', 1), (3, 'payments', 2), (4, 'reports', 2), (5, 'ui', 1);
    """)
    return conn


def fetch_all(conn: sqlite3.Connection, query: str):
    return [dict(row) for row in conn.execute(query).fetchall()]


def main() -> None:
    conn = build_demo_db()
    print(fetch_all(conn, """
        WITH RECURSIVE tree AS (
            SELECT id, name, parent_id, 0 AS depth FROM categories WHERE id = 1
            UNION ALL
            SELECT c.id, c.name, c.parent_id, tree.depth + 1
            FROM categories AS c
            INNER JOIN tree ON c.parent_id = tree.id
        )
        SELECT name, depth FROM tree ORDER BY depth, id
    """))


if __name__ == '__main__':
    main()
