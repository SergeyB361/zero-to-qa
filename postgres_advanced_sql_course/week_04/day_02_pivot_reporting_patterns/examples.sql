-- Pivot-like reporting patterns
SELECT executed_at::date AS run_day,
       COUNT(*) FILTER (WHERE status = 'passed') AS passed_runs,
       COUNT(*) FILTER (WHERE status = 'failed') AS failed_runs,
       COUNT(*) FILTER (WHERE status = 'blocked') AS blocked_runs
FROM test_runs
GROUP BY executed_at::date
ORDER BY run_day;

SELECT reported_by,
       COUNT(*) FILTER (WHERE severity = 'critical') AS critical_defects,
       COUNT(*) FILTER (WHERE severity = 'major') AS major_defects,
       COUNT(*) FILTER (WHERE severity = 'minor') AS minor_defects
FROM defects
GROUP BY reported_by
ORDER BY reported_by;
