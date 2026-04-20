-- Практика: index basics

-- Задание 1: index_for_tasks_status
-- Напиши CREATE INDEX для tasks(status).
-- expected: индекс по колонке status
CREATE INDEX IF NOT EXISTS idx_tasks_status_practice
ON tasks(status);

-- Задание 2: index_for_tasks_project_id
-- Напиши CREATE INDEX для tasks(project_id).
-- expected: индекс по колонке project_id
CREATE INDEX IF NOT EXISTS idx_tasks_project_id_practice
ON tasks(project_id);

-- Задание 3: index_for_defects_reported_at
-- Напиши CREATE INDEX для defects(reported_at).
-- expected: индекс по колонке reported_at
CREATE INDEX IF NOT EXISTS idx_defects_reported_at_practice
ON defects(reported_at);

-- Задание 4: explain_lookup_after_index
-- На TEMP TABLE создай индекс по status и покажи EXPLAIN для WHERE status = 'failed'.
-- expected: в решении есть CREATE INDEX и EXPLAIN одного lookup-запроса
DROP TABLE IF EXISTS explain_status_demo;
CREATE TEMP TABLE explain_status_demo AS
SELECT gs AS id,
       CASE WHEN gs % 10 = 0 THEN 'failed' ELSE 'passed' END AS status
FROM generate_series(1, 10000) AS gs;
CREATE INDEX idx_explain_status_demo_status
ON explain_status_demo(status);
EXPLAIN
SELECT *
FROM explain_status_demo
WHERE status = 'failed';

-- Задание 5: choose_index_candidates
-- Выбери 3 хорошие кандидатные колонки для индекса из dataset и кратко запиши их как комментарии в SQL.
-- expected: осмысленные колонки вроде status/project_id/reported_at/executed_by
-- candidate 1: tasks(status) useful for status-based dashboards and queue lookups
-- candidate 2: tasks(project_id) useful for joins and per-project reports
-- candidate 3: test_runs(executed_by) useful for executor-centric analytics and latest-run reports
SELECT 'index candidate notes completed' AS note;
