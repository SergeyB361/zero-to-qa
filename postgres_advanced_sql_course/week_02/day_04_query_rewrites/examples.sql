-- Query rewrites

-- Пример 1: correlated subquery -> join + aggregate.
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

-- Пример 2: repeated filtering -> CTE.
EXPLAIN
WITH active_reporters AS (
    SELECT id, name
    FROM users
    WHERE is_active IS TRUE
)
SELECT ar.name,
       COUNT(d.id) AS defects_count
FROM active_reporters AS ar
LEFT JOIN defects AS d ON d.reported_by = ar.id
GROUP BY ar.id, ar.name;

-- Пример 3: top run per executor через ranking вместо ручной логики.
EXPLAIN
WITH ranked_runs AS (
    SELECT id,
           executed_by,
           executed_at,
           ROW_NUMBER() OVER (PARTITION BY executed_by ORDER BY executed_at DESC) AS rn
    FROM test_runs
)
SELECT *
FROM ranked_runs
WHERE rn = 1;
