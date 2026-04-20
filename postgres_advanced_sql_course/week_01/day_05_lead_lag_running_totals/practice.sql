-- Практика: LEAD, LAG и running totals

-- Задание 1: previous_duration_by_run
-- Через LAG верни предыдущую длительность run по executed_at.
-- expected: NULL, 35.00, 41.00, 55.00
SELECT id,
       duration_seconds,
       LAG(duration_seconds) OVER (ORDER BY executed_at, id) AS previous_duration
FROM test_runs
ORDER BY executed_at, id;

-- Задание 2: next_status_by_run
-- Через LEAD верни следующий status по executed_at.
-- expected: failed, passed, blocked, NULL
SELECT id,
       status,
       LEAD(status) OVER (ORDER BY executed_at, id) AS next_status
FROM test_runs
ORDER BY executed_at, id;

-- Задание 3: running_duration_total
-- Построй running total по duration_seconds.
-- expected: 35.00, 76.00, 131.00, 143.00
SELECT id,
       duration_seconds,
       SUM(duration_seconds) OVER (ORDER BY executed_at, id ROWS UNBOUNDED PRECEDING) AS running_duration_total
FROM test_runs
ORDER BY executed_at, id;

-- Задание 4: gap_minutes_between_runs
-- Посчитай разницу в минутах между текущим executed_at и предыдущим через LAG.
-- expected: NULL, 30, 30, 20
SELECT id,
       EXTRACT(EPOCH FROM (
           executed_at - LAG(executed_at) OVER (ORDER BY executed_at, id)
       )) / 60 AS gap_minutes
FROM test_runs
ORDER BY executed_at, id;

-- Задание 5: duration_delta_vs_previous
-- Посчитай duration_seconds - previous_duration.
-- expected: NULL, 6.00, 14.00, -43.00
SELECT id,
       duration_seconds - LAG(duration_seconds) OVER (ORDER BY executed_at, id) AS duration_delta_vs_previous
FROM test_runs
ORDER BY executed_at, id;
