-- Практика: query rewrites

-- Задание 1: rewrite_project_task_count
-- Перепиши correlated subquery для tasks_count по проектам в join + aggregate.
-- expected: один вариант с подзапросом и один переписанный вариант
SELECT 'TODO: rewrite_project_task_count' AS todo;

-- Задание 2: rewrite_latest_run_per_executor
-- Реализуй latest run per executor через CTE + ROW_NUMBER().
-- expected: Anna -> 1, Boris -> 3, Oleg -> 4
SELECT 'TODO: rewrite_latest_run_per_executor' AS todo;

-- Задание 3: rewrite_open_defects_report
-- Вынеси open/in_progress defects в CTE и собери report по reporter.
-- expected: Anna -> 1, Boris -> 1
SELECT 'TODO: rewrite_open_defects_report' AS todo;

-- Задание 4: narrow_select_list
-- Покажи rewrite, где SELECT * заменён на осмысленный список колонок.
-- expected: два коротких варианта запроса: широкий и узкий
SELECT 'TODO: narrow_select_list' AS todo;

-- Задание 5: compare_plans_before_after_rewrite
-- Для одной своей переписанной задачи добавь EXPLAIN до и после.
-- expected: два EXPLAIN
SELECT 'TODO: compare_plans_before_after_rewrite' AS todo;
