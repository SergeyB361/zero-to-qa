-- Мини-проект: metrics report

-- runs_per_status
-- expected: blocked = 1, failed = 1, passed = 2
SELECT status,
       COUNT(*) AS runs_count
FROM test_runs
GROUP BY status
ORDER BY status;

-- avg_duration_per_case
-- expected: Create order = 41.0, Login works = 35.0, Profile update = 12.0, Refresh token = 55.0
SELECT c.title,
       ROUND(AVG(r.duration_seconds), 2) AS avg_duration
FROM test_runs AS r
JOIN test_cases AS c ON c.id = r.case_id
GROUP BY c.id, c.title
ORDER BY c.title;

-- tasks_per_project
-- expected: Mobile App = 1, Public API = 1, Web Portal = 2
SELECT p.name AS project_name,
       COUNT(t.id) AS tasks_count
FROM projects AS p
LEFT JOIN tasks AS t ON t.project_id = p.id
GROUP BY p.id, p.name
ORDER BY p.name;

-- open_defects_by_severity
-- expected: critical = 2
SELECT severity,
       COUNT(*) AS active_defects_count
FROM defects
WHERE status IN ('open', 'in_progress')
GROUP BY severity
ORDER BY severity;
