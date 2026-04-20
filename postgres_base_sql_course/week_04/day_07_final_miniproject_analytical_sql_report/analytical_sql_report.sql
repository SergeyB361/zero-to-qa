-- Финальный мини-проект: analytical SQL report
-- Цельный demo flow по базе zero_to_qa.

-- project_load_report
SELECT p.name AS project_name,
       COUNT(t.id) AS total_tasks,
       COUNT(*) FILTER (WHERE t.status <> 'closed') AS unfinished_tasks
FROM projects AS p
LEFT JOIN tasks AS t ON t.project_id = p.id
GROUP BY p.id, p.name
ORDER BY p.id;

-- run_status_report
SELECT (executed_at AT TIME ZONE 'Europe/Moscow')::date AS run_day,
       COUNT(*) AS total_runs,
       COUNT(*) FILTER (WHERE status = 'passed') AS passed_runs,
       COUNT(*) FILTER (WHERE status = 'failed') AS failed_runs,
       COUNT(*) FILTER (WHERE status = 'blocked') AS blocked_runs
FROM test_runs
GROUP BY run_day
ORDER BY run_day;

-- latest_executor_activity
SELECT DISTINCT ON (u.id)
       u.name,
       r.id AS latest_run_id,
       r.status,
       r.executed_at
FROM test_runs AS r
JOIN users AS u ON u.id = r.executed_by
ORDER BY u.id, r.executed_at DESC, r.id DESC;

-- open_defect_severity_report
SELECT severity,
       COUNT(*) AS open_defects_count,
       STRING_AGG(title, ', ' ORDER BY title) AS defect_titles
FROM defects
WHERE status IN ('open', 'in_progress')
GROUP BY severity
ORDER BY severity;
