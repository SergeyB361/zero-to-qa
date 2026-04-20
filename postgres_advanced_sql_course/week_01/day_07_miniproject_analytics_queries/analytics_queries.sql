-- Мини-проект: analytics queries
-- Собери цельный advanced SQL demo flow по базе zero_to_qa.

-- latest_executor_runs
WITH ranked_runs AS (
    SELECT r.id,
           r.executed_by,
           r.status,
           r.executed_at,
           ROW_NUMBER() OVER (PARTITION BY r.executed_by ORDER BY r.executed_at DESC, r.id DESC) AS rn
    FROM test_runs AS r
)
SELECT u.name,
       rr.id AS latest_run_id,
       rr.status,
       rr.executed_at
FROM ranked_runs AS rr
JOIN users AS u ON u.id = rr.executed_by
WHERE rr.rn = 1
ORDER BY u.name;

-- daily_run_calendar
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

-- project_points_ranking
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

-- reporter_defect_summary
SELECT u.name,
       COUNT(d.id) AS defects_count,
       STRING_AGG(d.title, ', ' ORDER BY d.title) AS defect_titles
FROM defects AS d
JOIN users AS u ON u.id = d.reported_by
GROUP BY u.id, u.name
ORDER BY u.name;
