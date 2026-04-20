-- Практика на advanced querying

-- Задание 1: latest_run_per_executor_report
-- Через CTE + ROW_NUMBER() верни последний run по каждому executor.
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

-- Задание 2: defect_summary_with_window
-- Верни defects и defects_per_reporter через COUNT(*) OVER (PARTITION BY reported_by).
-- expected: Anna -> 1, Boris -> 2
SELECT id,
       title,
       reported_by,
       COUNT(*) OVER (PARTITION BY reported_by) AS defects_per_reporter
FROM defects
ORDER BY id;

-- Задание 3: recursive_run_calendar_report
-- Построй календарь 2026-04-09 .. 2026-04-11 и посчитай runs_count по дням.
-- expected: 0, 4, 0
WITH RECURSIVE calendar AS (
    SELECT DATE '2026-04-09' AS day
    UNION ALL
    SELECT day + 1
    FROM calendar
    WHERE day < DATE '2026-04-11'
)
SELECT c.day,
       COUNT(r.id) AS runs_count
FROM calendar AS c
LEFT JOIN test_runs AS r
    ON (r.executed_at AT TIME ZONE 'Europe/Moscow')::date = c.day
GROUP BY c.day
ORDER BY c.day;

-- Задание 4: project_points_rank_report
-- Через CTE агрегируй total_points по проектам и затем посчитай RANK().
-- expected: Web Portal = 8 rank 1; Public API = 8 rank 1; Mobile App = 5 rank 3
WITH project_points AS (
    SELECT project_id,
           SUM(estimate_points) AS total_points
    FROM tasks
    GROUP BY project_id
)
SELECT p.name,
       pp.total_points,
       RANK() OVER (ORDER BY pp.total_points DESC) AS points_rank
FROM project_points AS pp
JOIN projects AS p ON p.id = pp.project_id
ORDER BY points_rank, p.name;

-- Задание 5: running_duration_report
-- Верни run id и running total duration_seconds по executed_at.
-- expected: 35.00, 76.00, 131.00, 143.00
SELECT id,
       SUM(duration_seconds) OVER (ORDER BY executed_at, id ROWS UNBOUNDED PRECEDING) AS running_duration_total
FROM test_runs
ORDER BY executed_at, id;
