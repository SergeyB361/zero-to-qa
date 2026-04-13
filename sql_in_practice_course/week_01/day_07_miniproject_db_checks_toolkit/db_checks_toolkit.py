# Финальный мини-проект: DB Checks Toolkit
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


def row_exists(conn: sqlite3.Connection, query: str) -> bool:
    """Верни True, если запрос возвращает хотя бы одну строку."""
    return False


def count_rows(conn: sqlite3.Connection, query: str) -> int:
    """Верни количество строк по запросу."""
    return -1


def get_scalar(conn: sqlite3.Connection, query: str):
    """Верни скалярное значение из запроса."""
    return -1


def status_distribution(
    conn: sqlite3.Connection, table_name: str, column_name: str
) -> dict[str, int]:
    """Верни словарь status -> count по таблице и колонке."""
    return {}


def main() -> None:
    conn = build_demo_db()
    critical_defect_query = """
        SELECT 1
        FROM defects
        WHERE severity = 'critical' AND status = 'open'
        LIMIT 1;
    """
    open_tasks_query = """
        SELECT id
        FROM tasks
        WHERE status = 'open';
    """
    failed_runs_query = """
        SELECT COUNT(*)
        FROM test_runs
        WHERE status = 'failed';
    """
    print('row_exists ->', row_exists(conn, critical_defect_query), '| expected:', 'True')
    print('count_rows ->', count_rows(conn, open_tasks_query), '| expected:', '3')
    print('get_scalar ->', get_scalar(conn, failed_runs_query), '| expected:', '2')
    print(
        'status_distribution ->',
        status_distribution(conn, 'test_runs', 'status'),
        '| expected:',
        "{'failed': 2, 'passed': 3, 'skipped': 1}",
    )
    print('Доведи функции до совпадения с expected и затем улучши формат вывода.')


if __name__ == "__main__":
    main()
