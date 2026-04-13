-- INNER JOIN
-- Выполни setup-часть, затем замени TODO-запросы своими решениями.

-- Setup dataset
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

-- Задание 1: task_assignees
-- Верни пары `task_id:name` для всех задач.
-- expected: "['1:Anna', '2:Oleg', '3:Boris', '4:Anna', '5:Nina']"
-- TODO: замени заглушку реальным SQL-запросом
SELECT 'TODO: task_assignees' AS todo;

-- Задание 2: project_owners
-- Верни пары `project_name:owner_name`.
-- expected: "['Mobile App:Nina', 'Public API:Boris', 'Web Portal:Anna']"
-- TODO: замени заглушку реальным SQL-запросом
SELECT 'TODO: project_owners' AS todo;

-- Задание 3: failed_case_titles
-- Верни названия test case, у которых были failed runs.
-- expected: "['Create order', 'Login works']"
-- TODO: замени заглушку реальным SQL-запросом
SELECT 'TODO: failed_case_titles' AS todo;

-- Задание 4: non_closed_task_projects
-- Верни названия проектов для задач со статусом не closed.
-- expected: "['Mobile App', 'Public API', 'Public API', 'Web Portal']"
-- TODO: замени заглушку реальным SQL-запросом
SELECT 'TODO: non_closed_task_projects' AS todo;

-- Задание 5: defects_with_authors
-- Верни пары defect:user в формате title:name.
-- expected: "['Login 500:Boris', 'Slow export:Oleg', 'Wrong total:Anna']"
-- TODO: замени заглушку реальным SQL-запросом
SELECT 'TODO: defects_with_authors' AS todo;
