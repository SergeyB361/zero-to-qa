# Recursive CTE
import sqlite3


def build_demo_db() -> sqlite3.Connection:
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row
    conn.executescript("""
    CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT NOT NULL, manager_id INTEGER);
    INSERT INTO employees VALUES (1, 'CTO', NULL), (2, 'QA Lead', 1), (3, 'Backend Lead', 1), (4, 'QA Engineer', 2), (5, 'Automation Engineer', 2);
    """)
    return conn


def management_chain(conn: sqlite3.Connection):
    return []


def qa_subtree(conn: sqlite3.Connection):
    return []


def main() -> None:
    conn = build_demo_db()
    print('management_chain ->', management_chain(conn), '| expected:', "['QA Engineer', 'QA Lead', 'CTO']")
    print('qa_subtree ->', qa_subtree(conn), '| expected:', "['Automation Engineer', 'QA Engineer', 'QA Lead']")


if __name__ == '__main__':
    main()
