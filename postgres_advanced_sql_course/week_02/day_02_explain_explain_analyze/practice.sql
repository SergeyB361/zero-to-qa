-- Практика: EXPLAIN и EXPLAIN ANALYZE

-- Задание 1: explain_open_tasks
-- Напиши EXPLAIN для запроса tasks со статусом open.
-- expected: есть EXPLAIN и SELECT по tasks
EXPLAIN
SELECT id, project_id, assignee_id
FROM tasks
WHERE status = 'open';

-- Задание 2: explain_analyze_test_runs_by_executor
-- Напиши EXPLAIN ANALYZE для COUNT(*) по test_runs WHERE executed_by = 2.
-- expected: есть EXPLAIN ANALYZE и агрегирующий запрос
EXPLAIN ANALYZE
SELECT COUNT(*)
FROM test_runs
WHERE executed_by = 2;

-- Задание 3: compare_before_after_index
-- На TEMP TABLE покажи план до и после CREATE INDEX по status.
-- expected: два EXPLAIN и один CREATE INDEX
DROP TABLE IF EXISTS explain_compare_demo;
CREATE TEMP TABLE explain_compare_demo AS
SELECT gs AS id,
       CASE WHEN gs % 10 = 0 THEN 'failed' ELSE 'passed' END AS status
FROM generate_series(1, 10000) AS gs;
EXPLAIN
SELECT * FROM explain_compare_demo WHERE status = 'failed';
CREATE INDEX idx_explain_compare_demo_status ON explain_compare_demo(status);
EXPLAIN
SELECT * FROM explain_compare_demo WHERE status = 'failed';

-- Задание 4: explain_join_query
-- Напиши EXPLAIN для join tasks -> projects.
-- expected: есть EXPLAIN и JOIN по project_id
EXPLAIN
SELECT t.id,
       p.name
FROM tasks AS t
JOIN projects AS p ON p.id = t.project_id;

-- Задание 5: analyze_group_by_query
-- Напиши EXPLAIN ANALYZE для GROUP BY по defects.status.
-- expected: есть EXPLAIN ANALYZE и GROUP BY
EXPLAIN ANALYZE
SELECT status,
       COUNT(*)
FROM defects
GROUP BY status;
