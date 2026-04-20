-- Практика: date/time queries

-- Задание 1: defect_report_days
-- Верни id и reported_at::date по defects.
-- expected: у всех строк дата 2026-04-09
SELECT id,
       (reported_at AT TIME ZONE 'Europe/Moscow')::date AS reported_day
FROM defects
ORDER BY id;

-- Задание 2: runs_per_hour_bucket
-- Посчитай количество test_runs по DATE_TRUNC('hour', executed_at).
-- expected: 2026-04-10 10:00:00 -> 2, 2026-04-10 11:00:00 -> 2
SELECT DATE_TRUNC('hour', executed_at AT TIME ZONE 'Europe/Moscow') AS hour_bucket,
       COUNT(*) AS runs_count
FROM test_runs
GROUP BY hour_bucket
ORDER BY hour_bucket;

-- Задание 3: extract_run_hours
-- Верни id и EXTRACT(HOUR FROM executed_at) по test_runs.
-- expected: часы 10, 10, 11, 11
SELECT id,
       EXTRACT(HOUR FROM executed_at AT TIME ZONE 'Europe/Moscow') AS executed_hour
FROM test_runs
ORDER BY id;

-- Задание 4: closed_days_from_april_start
-- Для закрытых задач посчитай closed_at::date - DATE '2026-04-01'.
-- expected: для task id = 2 результат 2
SELECT id,
       ((closed_at AT TIME ZONE 'Europe/Moscow')::date - DATE '2026-04-01') AS days_from_april_start
FROM tasks
WHERE closed_at IS NOT NULL
ORDER BY id;

-- Задание 5: run_plus_two_hours
-- Верни id и executed_at + INTERVAL '2 hours'.
-- expected: для run id = 4 время становится 2026-04-10 13:20:00
SELECT id,
       (executed_at AT TIME ZONE 'Europe/Moscow') + INTERVAL '2 hours' AS executed_plus_two_hours
FROM test_runs
ORDER BY id;
