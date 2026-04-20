-- Практика: time-series analytics

-- Задание 1: daily_runs_summary
-- Сведи test_runs по дням.
SELECT executed_at::date AS run_day,
       COUNT(*) AS total_runs,
       ROUND(AVG(duration_seconds), 2) AS avg_duration
FROM test_runs
GROUP BY executed_at::date
ORDER BY run_day;

-- Задание 2: hourly_runs_buckets
-- Сведи test_runs по часам.
SELECT DATE_TRUNC('hour', executed_at) AS run_hour,
       COUNT(*) AS runs_count
FROM test_runs
GROUP BY DATE_TRUNC('hour', executed_at)
ORDER BY run_hour;

-- Задание 3: daily_defect_inflow
-- Сведи приход defects по дням.
SELECT reported_at::date AS defect_day,
       COUNT(*) AS defects_count
FROM defects
GROUP BY reported_at::date
ORDER BY defect_day;

-- Задание 4: calendar_with_zero_days
-- Построй календарь с днями без test_runs.
WITH RECURSIVE calendar AS (
    SELECT DATE '2026-04-09' AS day
    UNION ALL
    SELECT day + 1
    FROM calendar
    WHERE day < DATE '2026-04-12'
)
SELECT c.day,
       COUNT(tr.id) AS runs_count
FROM calendar AS c
LEFT JOIN test_runs AS tr ON tr.executed_at::date = c.day
GROUP BY c.day
ORDER BY c.day;

-- Задание 5: cumulative_runs_by_time
-- Посчитай cumulative total по дням.
WITH RECURSIVE calendar AS (
    SELECT DATE '2026-04-09' AS day
    UNION ALL
    SELECT day + 1
    FROM calendar
    WHERE day < DATE '2026-04-12'
),
daily_runs AS (
    SELECT executed_at::date AS run_day,
           COUNT(*) AS runs_count
    FROM test_runs
    GROUP BY executed_at::date
)
SELECT c.day,
       COALESCE(dr.runs_count, 0) AS runs_count,
       SUM(COALESCE(dr.runs_count, 0)) OVER (ORDER BY c.day) AS cumulative_runs
FROM calendar AS c
LEFT JOIN daily_runs AS dr ON dr.run_day = c.day
ORDER BY c.day;
