-- LEAD, LAG и running totals

-- Пример 1: предыдущее значение duration_seconds.
SELECT id,
       executed_at,
       duration_seconds,
       LAG(duration_seconds) OVER (ORDER BY executed_at) AS previous_duration
FROM test_runs
ORDER BY executed_at;

-- Пример 2: следующий статус run.
SELECT id,
       status,
       LEAD(status) OVER (ORDER BY executed_at) AS next_status
FROM test_runs
ORDER BY executed_at;

-- Пример 3: running total по длительности runs.
SELECT id,
       executed_at,
       duration_seconds,
       SUM(duration_seconds) OVER (
           ORDER BY executed_at
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS running_duration_total
FROM test_runs
ORDER BY executed_at;

-- Пример 4: разница с предыдущим значением.
SELECT id,
       duration_seconds,
       duration_seconds - LAG(duration_seconds) OVER (ORDER BY executed_at) AS delta_vs_previous
FROM test_runs
ORDER BY executed_at;
