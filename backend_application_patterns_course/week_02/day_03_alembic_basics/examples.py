import sqlite3


UPGRADE_STEPS = [
    "ALTER TABLE projects ADD COLUMN status TEXT DEFAULT 'draft'",
    "UPDATE projects SET status = 'active' WHERE title = 'Portal'",
]


def show_columns(connection: sqlite3.Connection, table_name: str) -> list[str]:
    rows = connection.execute(f'PRAGMA table_info({table_name})').fetchall()
    return [row[1] for row in rows]


if __name__ == '__main__':
    connection = sqlite3.connect(':memory:')
    connection.execute('CREATE TABLE projects (id INTEGER PRIMARY KEY, title TEXT NOT NULL)')
    connection.execute("INSERT INTO projects (title) VALUES ('Portal'), ('Billing')")

    print('BEFORE COLUMNS ->', show_columns(connection, 'projects'))
    print('BEFORE ROWS ->', connection.execute('SELECT id, title FROM projects ORDER BY id').fetchall())

    for step in UPGRADE_STEPS:
        connection.execute(step)

    print('AFTER COLUMNS ->', show_columns(connection, 'projects'))
    print('AFTER ROWS ->', connection.execute('SELECT id, title, status FROM projects ORDER BY id').fetchall())
    print('MEANING -> these SQL steps would live inside Alembic upgrade()')
