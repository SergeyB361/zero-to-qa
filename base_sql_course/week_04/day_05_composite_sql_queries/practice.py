# Композитные SQL-запросы
import sqlite3


def build_demo_db() -> sqlite3.Connection:
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row
    conn.executescript("""
    CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL, team TEXT NOT NULL);
    CREATE TABLE projects (id INTEGER PRIMARY KEY, name TEXT NOT NULL, owner_id INTEGER NOT NULL, FOREIGN KEY(owner_id) REFERENCES users(id));
    CREATE TABLE tasks (id INTEGER PRIMARY KEY, project_id INTEGER NOT NULL, assignee_id INTEGER NOT NULL, status TEXT NOT NULL, priority TEXT NOT NULL, estimate_hours INTEGER NOT NULL, FOREIGN KEY(project_id) REFERENCES projects(id), FOREIGN KEY(assignee_id) REFERENCES users(id));
    INSERT INTO users VALUES (1, 'Anna', 'web'), (2, 'Boris', 'api'), (3, 'Nina', 'mobile');
    INSERT INTO projects VALUES (1, 'Portal', 1), (2, 'API', 2), (3, 'Mobile', 3);
    INSERT INTO tasks VALUES
        (1, 1, 1, 'open', 'high', 5),
        (2, 1, 1, 'closed', 'low', 2),
        (3, 2, 2, 'open', 'high', 8),
        (4, 2, 1, 'open', 'medium', 3),
        (5, 3, 3, 'open', 'medium', 6);
    """)
    return conn


def open_tasks_per_project(conn: sqlite3.Connection):
    return []


def heavy_projects(conn: sqlite3.Connection):
    return []


def owners_with_open_work(conn: sqlite3.Connection):
    return []


def main() -> None:
    conn = build_demo_db()
    print('open_tasks_per_project ->', open_tasks_per_project(conn), '| expected:', "['API:2', 'Mobile:1', 'Portal:1']")
    print('heavy_projects ->', heavy_projects(conn), '| expected:', "['API', 'Mobile']")
    print('owners_with_open_work ->', owners_with_open_work(conn), '| expected:', "['Anna:1', 'Boris:2', 'Nina:1']")


if __name__ == '__main__':
    main()
