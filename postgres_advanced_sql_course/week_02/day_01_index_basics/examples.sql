-- Index basics
-- Примеры безопасны для повторного запуска: всё делается на TEMP TABLE.

CREATE TEMP TABLE perf_runs AS
SELECT gs AS id,
       CASE WHEN gs % 10 = 0 THEN 'failed' ELSE 'passed' END AS status,
       (gs % 4) + 1 AS executed_by,
       NOW() - (gs || ' minutes')::interval AS executed_at
FROM generate_series(1, 50000) AS gs;

-- Пример 1: план без индекса.
EXPLAIN
SELECT *
FROM perf_runs
WHERE status = 'failed';

-- Пример 2: добавляем индекс и смотрим план снова.
CREATE INDEX idx_perf_runs_status ON perf_runs(status);

EXPLAIN
SELECT *
FROM perf_runs
WHERE status = 'failed';

-- Пример 3: индекс по колонке join/filter.
CREATE INDEX idx_perf_runs_executed_by ON perf_runs(executed_by);

EXPLAIN
SELECT COUNT(*)
FROM perf_runs
WHERE executed_by = 2;
