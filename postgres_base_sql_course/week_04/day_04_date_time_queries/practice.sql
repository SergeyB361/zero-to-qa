-- Практика: date/time queries

-- Задание 1: defect_report_days
-- Верни id и reported_at::date по defects.
-- expected: у всех строк дата 2026-04-09
SELECT 'TODO: defect_report_days' AS todo;

-- Задание 2: runs_per_hour_bucket
-- Посчитай количество test_runs по DATE_TRUNC('hour', executed_at).
-- expected: 2026-04-10 10:00:00+03 -> 2, 2026-04-10 11:00:00+03 -> 2
SELECT 'TODO: runs_per_hour_bucket' AS todo;

-- Задание 3: extract_run_hours
-- Верни id и EXTRACT(HOUR FROM executed_at) по test_runs.
-- expected: часы 10, 10, 11, 11
SELECT 'TODO: extract_run_hours' AS todo;

-- Задание 4: closed_days_from_april_start
-- Для закрытых задач посчитай closed_at::date - DATE '2026-04-01'.
-- expected: для task id = 2 результат 2
SELECT 'TODO: closed_days_from_april_start' AS todo;

-- Задание 5: run_plus_two_hours
-- Верни id и executed_at + INTERVAL '2 hours'.
-- expected: для run id = 4 время становится 2026-04-10 13:20:00+03
SELECT 'TODO: run_plus_two_hours' AS todo;
