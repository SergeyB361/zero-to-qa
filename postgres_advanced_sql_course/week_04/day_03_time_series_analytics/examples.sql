-- Time-series analytics
SELECT executed_at::date AS run_day,
       COUNT(*) AS total_runs,
       AVG(duration_seconds) AS avg_duration
FROM test_runs
GROUP BY executed_at::date
ORDER BY run_day;

SELECT DATE_TRUNC('hour', executed_at) AS run_hour,
       COUNT(*) AS runs_count
FROM test_runs
GROUP BY DATE_TRUNC('hour', executed_at)
ORDER BY run_hour;

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
