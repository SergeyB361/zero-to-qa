-- Практика: index basics

-- Задание 1: index_for_tasks_status
-- Напиши CREATE INDEX для tasks(status).
-- expected: индекс по колонке status
SELECT 'TODO: index_for_tasks_status' AS todo;

-- Задание 2: index_for_tasks_project_id
-- Напиши CREATE INDEX для tasks(project_id).
-- expected: индекс по колонке project_id
SELECT 'TODO: index_for_tasks_project_id' AS todo;

-- Задание 3: index_for_defects_reported_at
-- Напиши CREATE INDEX для defects(reported_at).
-- expected: индекс по колонке reported_at
SELECT 'TODO: index_for_defects_reported_at' AS todo;

-- Задание 4: explain_lookup_after_index
-- На TEMP TABLE создай индекс по status и покажи EXPLAIN для WHERE status = 'failed'.
-- expected: в решении есть CREATE INDEX и EXPLAIN одного lookup-запроса
SELECT 'TODO: explain_lookup_after_index' AS todo;

-- Задание 5: choose_index_candidates
-- Выбери 3 хорошие кандидатные колонки для индекса из dataset и кратко запиши их как комментарии в SQL.
-- expected: осмысленные колонки вроде status/project_id/reported_at/executed_by
SELECT 'TODO: choose_index_candidates' AS todo;
