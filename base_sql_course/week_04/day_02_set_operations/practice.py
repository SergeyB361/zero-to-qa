# UNION, UNION ALL, INTERSECT, EXCEPT
import sqlite3


def build_demo_db() -> sqlite3.Connection:
    conn = sqlite3.connect(':memory:')
    conn.executescript("""
    CREATE TABLE release_101_failed (title TEXT NOT NULL);
    CREATE TABLE release_102_failed (title TEXT NOT NULL);
    INSERT INTO release_101_failed VALUES ('Login works'), ('Create order'), ('Refund order');
    INSERT INTO release_102_failed VALUES ('Create order'), ('Filter products'), ('Refund order'), ('Refund order');
    """)
    return conn


def all_failed_titles(conn: sqlite3.Connection):
    return []


def repeated_failures(conn: sqlite3.Connection):
    return []


def only_first_release_failures(conn: sqlite3.Connection):
    return []


def main() -> None:
    conn = build_demo_db()
    print('all_failed_titles ->', all_failed_titles(conn), '| expected:', "['Create order', 'Filter products', 'Login works', 'Refund order']")
    print('repeated_failures ->', repeated_failures(conn), '| expected:', "['Create order', 'Refund order']")
    print('only_first_release_failures ->', only_first_release_failures(conn), '| expected:', "['Login works']")


if __name__ == '__main__':
    main()
