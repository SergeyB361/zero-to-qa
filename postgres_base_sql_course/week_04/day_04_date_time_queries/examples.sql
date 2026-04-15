-- Date/time queries

-- Пример 1: оставить только дату для reported_at.
SELECT id,
       title,
       reported_at::date AS reported_day
FROM defects
ORDER BY id;

-- Пример 2: сгруппировать test_runs по часовым bucket.
SELECT DATE_TRUNC('hour', executed_at) AS executed_hour,
       COUNT(*) AS runs_count
FROM test_runs
GROUP BY DATE_TRUNC('hour', executed_at)
ORDER BY executed_hour;

-- Пример 3: достать час выполнения через EXTRACT.
SELECT id,
       executed_at,
       EXTRACT(HOUR FROM executed_at) AS executed_hour
FROM test_runs
ORDER BY id;

-- Пример 4: прибавить 2 часа к executed_at.
SELECT id,
       executed_at,
       executed_at + INTERVAL '2 hours' AS plus_two_hours
FROM test_runs
ORDER BY id;
