-- Практика: EXPLAIN и EXPLAIN ANALYZE

-- Задание 1: explain_open_tasks
-- Напиши EXPLAIN для запроса tasks со статусом open.
-- expected: есть EXPLAIN и SELECT по tasks
SELECT 'TODO: explain_open_tasks' AS todo;

-- Задание 2: explain_analyze_test_runs_by_executor
-- Напиши EXPLAIN ANALYZE для COUNT(*) по test_runs WHERE executed_by = 2.
-- expected: есть EXPLAIN ANALYZE и агрегирующий запрос
SELECT 'TODO: explain_analyze_test_runs_by_executor' AS todo;

-- Задание 3: compare_before_after_index
-- На TEMP TABLE покажи план до и после CREATE INDEX по status.
-- expected: два EXPLAIN и один CREATE INDEX
SELECT 'TODO: compare_before_after_index' AS todo;

-- Задание 4: explain_join_query
-- Напиши EXPLAIN для join tasks -> projects.
-- expected: есть EXPLAIN и JOIN по project_id
SELECT 'TODO: explain_join_query' AS todo;

-- Задание 5: analyze_group_by_query
-- Напиши EXPLAIN ANALYZE для GROUP BY по defects.status.
-- expected: есть EXPLAIN ANALYZE и GROUP BY
SELECT 'TODO: analyze_group_by_query' AS todo;
