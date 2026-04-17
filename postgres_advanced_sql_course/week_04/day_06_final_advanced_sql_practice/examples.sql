-- Финальная advanced SQL-практика
WITH ranked_runs AS (
    SELECT id,
           executed_by,
           status,
           executed_at,
           ROW_NUMBER() OVER (PARTITION BY executed_by ORDER BY executed_at DESC) AS rn
    FROM test_runs
)
SELECT u.name,
       r.id AS latest_run_id,
       r.status,
       r.executed_at
FROM ranked_runs AS r
JOIN users AS u ON u.id = r.executed_by
WHERE r.rn = 1
ORDER BY u.name;

SELECT reported_by,
       COUNT(*) FILTER (WHERE severity = 'critical') AS critical_cnt,
       COUNT(*) FILTER (WHERE status IN ('open', 'in_progress')) AS active_cnt
FROM defects
GROUP BY reported_by
ORDER BY reported_by;
