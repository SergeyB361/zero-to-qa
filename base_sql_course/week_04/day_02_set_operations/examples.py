# UNION, UNION ALL, INTERSECT, EXCEPT
import sqlite3


def build_demo_db() -> sqlite3.Connection:
    conn = sqlite3.connect(':memory:')
    conn.executescript("""
    CREATE TABLE web_owners (name TEXT NOT NULL);
    CREATE TABLE api_owners (name TEXT NOT NULL);
    INSERT INTO web_owners VALUES ('Anna'), ('Oleg'), ('Nina');
    INSERT INTO api_owners VALUES ('Boris'), ('Anna'), ('Nina'), ('Nina');
    """)
    return conn


def fetch_list(conn: sqlite3.Connection, query: str):
    return [row[0] for row in conn.execute(query).fetchall()]


def main() -> None:
    conn = build_demo_db()
    print('UNION ->', fetch_list(conn, "SELECT name FROM web_owners UNION SELECT name FROM api_owners ORDER BY name"))
    print('UNION ALL ->', fetch_list(conn, "SELECT name FROM web_owners UNION ALL SELECT name FROM api_owners ORDER BY name"))
    print('INTERSECT ->', fetch_list(conn, "SELECT name FROM web_owners INTERSECT SELECT name FROM api_owners ORDER BY name"))
    print('EXCEPT ->', fetch_list(conn, "SELECT name FROM web_owners EXCEPT SELECT name FROM api_owners ORDER BY name"))


if __name__ == '__main__':
    main()
