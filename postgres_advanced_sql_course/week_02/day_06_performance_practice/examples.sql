-- Практика на performance: representative examples

-- Пример 1: lookup с индексом.
CREATE TEMP TABLE perf_cases AS
SELECT gs AS id,
       CASE WHEN gs % 5 = 0 THEN 'critical' ELSE 'high' END AS priority,
       CASE WHEN gs % 3 = 0 THEN 'api' ELSE 'auth' END AS area
FROM generate_series(1, 60000) AS gs;

EXPLAIN
SELECT *
FROM perf_cases
WHERE priority = 'critical';

CREATE INDEX idx_perf_cases_priority ON perf_cases(priority);

EXPLAIN
SELECT *
FROM perf_cases
WHERE priority = 'critical';

-- Пример 2: anti-pattern rewrite на времени.
EXPLAIN
SELECT id
FROM test_runs
WHERE DATE(executed_at) = DATE '2026-04-10';

EXPLAIN
SELECT id
FROM test_runs
WHERE executed_at >= TIMESTAMPTZ '2026-04-10 00:00:00+03'
  AND executed_at < TIMESTAMPTZ '2026-04-11 00:00:00+03';
