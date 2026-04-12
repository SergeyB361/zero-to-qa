# LEFT JOIN
import sqlite3


def build_demo_db() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    conn.executescript(
        """
        PRAGMA foreign_keys = ON;
        CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL, team TEXT NOT NULL, is_active INTEGER NOT NULL);
        CREATE TABLE projects (id INTEGER PRIMARY KEY, name TEXT NOT NULL, owner_id INTEGER NOT NULL, FOREIGN KEY(owner_id) REFERENCES users(id));
        CREATE TABLE tasks (id INTEGER PRIMARY KEY, project_id INTEGER NOT NULL, assignee_id INTEGER NOT NULL, status TEXT NOT NULL, priority TEXT NOT NULL, estimate_hours INTEGER NOT NULL, closed_at TEXT, FOREIGN KEY(project_id) REFERENCES projects(id), FOREIGN KEY(assignee_id) REFERENCES users(id));
        CREATE TABLE test_cases (id INTEGER PRIMARY KEY, title TEXT NOT NULL, area TEXT NOT NULL, priority TEXT NOT NULL);
        CREATE TABLE test_runs (id INTEGER PRIMARY KEY, case_id INTEGER NOT NULL, status TEXT NOT NULL, executed_by INTEGER NOT NULL, duration_sec INTEGER NOT NULL, FOREIGN KEY(case_id) REFERENCES test_cases(id), FOREIGN KEY(executed_by) REFERENCES users(id));
        CREATE TABLE defects (id INTEGER PRIMARY KEY, title TEXT NOT NULL, severity TEXT NOT NULL, status TEXT NOT NULL, created_by INTEGER NOT NULL, resolved_at TEXT, FOREIGN KEY(created_by) REFERENCES users(id));
        INSERT INTO users VALUES (1, 'Anna', 'web', 1), (2, 'Boris', 'api', 1), (3, 'Nina', 'mobile', 0), (4, 'Oleg', 'web', 1);
        INSERT INTO projects VALUES (1, 'Web Portal', 1), (2, 'Public API', 2), (3, 'Mobile App', 3);
        INSERT INTO tasks VALUES (1, 1, 1, 'open', 'high', 5, NULL), (2, 1, 4, 'closed', 'medium', 3, '2026-04-01'), (3, 2, 2, 'in_progress', 'high', 8, NULL), (4, 2, 1, 'open', 'low', 2, NULL), (5, 3, 3, 'open', 'medium', 13, NULL);
        INSERT INTO test_cases VALUES (1, 'Login works', 'auth', 'high'), (2, 'Create order', 'checkout', 'high'), (3, 'Filter products', 'catalog', 'medium'), (4, 'Export report', 'admin', 'low');
        INSERT INTO test_runs VALUES (1, 1, 'passed', 1, 35), (2, 1, 'failed', 2, 41), (3, 2, 'passed', 2, 55), (4, 3, 'skipped', 1, 0), (5, 4, 'passed', 4, 70), (6, 2, 'failed', 1, 60);
        INSERT INTO defects VALUES (1, 'Login 500', 'critical', 'open', 2, NULL), (2, 'Wrong total', 'major', 'closed', 1, '2026-04-05'), (3, 'Slow export', 'minor', 'open', 4, NULL);
        """
    )
    return conn


def fetch_all(conn: sqlite3.Connection, query: str):
    return [dict(row) for row in conn.execute(query).fetchall()]


def projects_with_task_counts(conn: sqlite3.Connection):
    """Верни пары `project:count` для проектов."""
    # Напиши SQL-запрос и выполни его через conn.execute(...).
    return []


def users_with_defect_counts(conn: sqlite3.Connection):
    """Верни пары `user:count` для количества созданных дефектов."""
    # Напиши SQL-запрос и выполни его через conn.execute(...).
    return []


def cases_with_run_counts(conn: sqlite3.Connection):
    """Верни пары `case:count` для количества запусков."""
    # Напиши SQL-запрос и выполни его через conn.execute(...).
    return []


def main() -> None:
    conn = build_demo_db()
    print('projects_with_task_counts ->', projects_with_task_counts(conn), '| expected:', "['Mobile App:1', 'Public API:2', 'Web Portal:2']")
    print('users_with_defect_counts ->', users_with_defect_counts(conn), '| expected:', "['Anna:1', 'Boris:1', 'Nina:0', 'Oleg:1']")
    print('cases_with_run_counts ->', cases_with_run_counts(conn), '| expected:', "['Login works:2', 'Create order:2', 'Filter products:1', 'Export report:1']")
    print('Добейся совпадения с expected, затем перечитай SQL глазами.')


if __name__ == "__main__":
    main()
