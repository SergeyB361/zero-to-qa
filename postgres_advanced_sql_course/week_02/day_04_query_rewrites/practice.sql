-- Практика: query rewrites

-- Задание 1: rewrite_project_task_count
-- Перепиши correlated subquery для tasks_count по проектам в join + aggregate.
-- expected: один вариант с подзапросом и один переписанный вариант
SELECT p.name,
       (
           SELECT COUNT(*)
           FROM tasks AS t
           WHERE t.project_id = p.id
       ) AS tasks_count
FROM projects AS p
ORDER BY p.id;

SELECT p.name,
       COUNT(t.id) AS tasks_count
FROM projects AS p
LEFT JOIN tasks AS t ON t.project_id = p.id
GROUP BY p.id, p.name
ORDER BY p.id;

-- Задание 2: rewrite_latest_run_per_executor
-- Реализуй latest run per executor через CTE + ROW_NUMBER().
-- expected: Anna -> 1, Boris -> 3, Oleg -> 4
WITH ranked_runs AS (
    SELECT r.id,
           r.executed_by,
           ROW_NUMBER() OVER (PARTITION BY r.executed_by ORDER BY r.executed_at DESC, r.id DESC) AS rn
    FROM test_runs AS r
)
SELECT u.name,
       rr.id AS latest_run_id
FROM ranked_runs AS rr
JOIN users AS u ON u.id = rr.executed_by
WHERE rr.rn = 1
ORDER BY u.name;

-- Задание 3: rewrite_open_defects_report
-- Вынеси open/in_progress defects в CTE и собери report по reporter.
-- expected: Anna -> 1, Boris -> 1
WITH active_defects AS (
    SELECT reported_by,
           COUNT(*) AS active_defects_count
    FROM defects
    WHERE status IN ('open', 'in_progress')
    GROUP BY reported_by
)
SELECT u.name,
       ad.active_defects_count
FROM active_defects AS ad
JOIN users AS u ON u.id = ad.reported_by
ORDER BY u.name;

-- Задание 4: narrow_select_list
-- Покажи rewrite, где SELECT * заменён на осмысленный список колонок.
-- expected: два коротких варианта запроса: широкий и узкий
SELECT *
FROM test_runs
WHERE status = 'failed';

SELECT id, case_id, executed_by, executed_at
FROM test_runs
WHERE status = 'failed';

-- Задание 5: compare_plans_before_after_rewrite
-- Для одной своей переписанной задачи добавь EXPLAIN до и после.
-- expected: два EXPLAIN
EXPLAIN
SELECT p.name,
       (
           SELECT COUNT(*)
           FROM tasks AS t
           WHERE t.project_id = p.id
       ) AS tasks_count
FROM projects AS p;

EXPLAIN
SELECT p.name,
       COUNT(t.id) AS tasks_count
FROM projects AS p
LEFT JOIN tasks AS t ON t.project_id = p.id
GROUP BY p.id, p.name;
