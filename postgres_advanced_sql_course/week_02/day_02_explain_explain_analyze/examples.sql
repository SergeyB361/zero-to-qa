-- EXPLAIN и EXPLAIN ANALYZE

CREATE TEMP TABLE perf_defects AS
SELECT gs AS id,
       CASE WHEN gs % 8 = 0 THEN 'critical' ELSE 'major' END AS severity,
       CASE WHEN gs % 9 = 0 THEN 'open' ELSE 'fixed' END AS status,
       NOW() - (gs || ' minutes')::interval AS reported_at
FROM generate_series(1, 40000) AS gs;

-- Пример 1: базовый план.
EXPLAIN
SELECT *
FROM perf_defects
WHERE status = 'open';

-- Пример 2: с индексом и EXPLAIN.
CREATE INDEX idx_perf_defects_status ON perf_defects(status);

EXPLAIN
SELECT *
FROM perf_defects
WHERE status = 'open';

-- Пример 3: EXPLAIN ANALYZE на агрегирующем запросе.
EXPLAIN ANALYZE
SELECT status, COUNT(*)
FROM perf_defects
GROUP BY status;
