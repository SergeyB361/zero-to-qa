-- Финальный мини-проект: Analytical SQL Report
-- Итоговый SQL-скрипт мини-проекта.

-- Setup dataset
CREATE TABLE projects (id INTEGER PRIMARY KEY, name TEXT NOT NULL);
    CREATE TABLE tasks (id INTEGER PRIMARY KEY, project_id INTEGER NOT NULL, status TEXT NOT NULL, priority TEXT NOT NULL, estimate_hours INTEGER NOT NULL, FOREIGN KEY(project_id) REFERENCES projects(id));
    CREATE TABLE test_runs (id INTEGER PRIMARY KEY, project_id INTEGER NOT NULL, status TEXT NOT NULL, executed_at TEXT NOT NULL, FOREIGN KEY(project_id) REFERENCES projects(id));
    INSERT INTO projects VALUES (1, 'Portal'), (2, 'API'), (3, 'Mobile');
    INSERT INTO tasks VALUES
        (1, 1, 'open', 'high', 5),
        (2, 1, 'closed', 'low', 2),
        (3, 2, 'open', 'high', 8),
        (4, 2, 'open', 'medium', 3),
        (5, 3, 'closed', 'low', 1);
    INSERT INTO test_runs VALUES
        (1, 1, 'passed', '2026-04-01 10:00:00'),
        (2, 1, 'failed', '2026-04-01 11:00:00'),
        (3, 2, 'passed', '2026-04-02 09:00:00'),
        (4, 2, 'failed', '2026-04-02 11:00:00');

-- Deliverable 1: project_load_report
-- project load report
-- expected: "['API:2:11', 'Portal:1:5']"
-- TODO: напиши итоговый SQL-запрос
SELECT 'TODO: project_load_report' AS todo;

-- Deliverable 2: priority_mix_report
-- priority mix report
-- expected: "{'high': 2, 'medium': 1, 'low': 0}"
-- TODO: напиши итоговый SQL-запрос
SELECT 'TODO: priority_mix_report' AS todo;

-- Deliverable 3: daily_run_report
-- daily run report
-- expected: "['2026-04-01:2', '2026-04-02:2']"
-- TODO: напиши итоговый SQL-запрос
SELECT 'TODO: daily_run_report' AS todo;
