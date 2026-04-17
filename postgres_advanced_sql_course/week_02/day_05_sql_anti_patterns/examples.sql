-- SQL anti-patterns

-- Пример 1: SELECT * vs narrow select list.
EXPLAIN
SELECT *
FROM test_runs
WHERE status = 'passed';

EXPLAIN
SELECT id, status, executed_at
FROM test_runs
WHERE status = 'passed';

-- Пример 2: функция на колонке vs диапазон времени.
EXPLAIN
SELECT id
FROM test_runs
WHERE DATE(executed_at) = DATE '2026-04-10';

EXPLAIN
SELECT id
FROM test_runs
WHERE executed_at >= TIMESTAMPTZ '2026-04-10 00:00:00+03'
  AND executed_at < TIMESTAMPTZ '2026-04-11 00:00:00+03';

-- Пример 3: DISTINCT как костыль.
EXPLAIN
SELECT DISTINCT p.name
FROM projects AS p
JOIN tasks AS t ON t.project_id = p.id;

EXPLAIN
SELECT p.name
FROM projects AS p
WHERE EXISTS (
    SELECT 1
    FROM tasks AS t
    WHERE t.project_id = p.id
);
