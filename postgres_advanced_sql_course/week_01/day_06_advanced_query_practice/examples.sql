-- Практика на advanced querying: примеры составных запросов

-- Пример 1: последний run по каждому executor через CTE + row_number.
WITH ranked_runs AS (
    SELECT id,
           executed_by,
           status,
           executed_at,
           ROW_NUMBER() OVER (PARTITION BY executed_by ORDER BY executed_at DESC) AS rn
    FROM test_runs
)
SELECT u.name,
       r.id AS latest_run_id,
       r.status,
       r.executed_at
FROM ranked_runs AS r
JOIN users AS u ON u.id = r.executed_by
WHERE r.rn = 1
ORDER BY u.name;

-- Пример 2: календарь + runs_count.
WITH RECURSIVE calendar AS (
    SELECT DATE '2026-04-09' AS day
    UNION ALL
    SELECT day + 1
    FROM calendar
    WHERE day < DATE '2026-04-11'
)
SELECT c.day,
       COUNT(tr.id) AS runs_count
FROM calendar AS c
LEFT JOIN test_runs AS tr ON tr.executed_at::date = c.day
GROUP BY c.day
ORDER BY c.day;

-- Пример 3: ранжирование проектов по total estimate_points.
WITH project_points AS (
    SELECT p.id,
           p.name,
           SUM(t.estimate_points) AS total_points
    FROM projects AS p
    JOIN tasks AS t ON t.project_id = p.id
    GROUP BY p.id, p.name
)
SELECT name,
       total_points,
       RANK() OVER (ORDER BY total_points DESC) AS project_rank
FROM project_points
ORDER BY project_rank, name;
