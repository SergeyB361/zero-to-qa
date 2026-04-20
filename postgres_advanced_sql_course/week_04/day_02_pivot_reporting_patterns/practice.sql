-- Практика: pivot-like reporting patterns

-- Задание 1: run_status_pivot
-- Сведи статусы test_runs по дням.
SELECT executed_at::date AS run_day,
       COUNT(*) FILTER (WHERE status = 'passed') AS passed_runs,
       COUNT(*) FILTER (WHERE status = 'failed') AS failed_runs,
       COUNT(*) FILTER (WHERE status = 'blocked') AS blocked_runs
FROM test_runs
GROUP BY executed_at::date
ORDER BY run_day;

-- Задание 2: defect_severity_pivot_by_reporter
-- Сведи severity по reporter.
SELECT u.name,
       COUNT(d.id) FILTER (WHERE d.severity = 'critical') AS critical_defects,
       COUNT(d.id) FILTER (WHERE d.severity = 'major') AS major_defects,
       COUNT(d.id) FILTER (WHERE d.severity = 'minor') AS minor_defects
FROM users AS u
LEFT JOIN defects AS d ON d.reported_by = u.id
GROUP BY u.id, u.name
ORDER BY u.name;

-- Задание 3: task_status_pivot_by_project
-- Сведи статусы задач по проектам.
SELECT p.name,
       COUNT(t.id) FILTER (WHERE t.status = 'open') AS open_tasks,
       COUNT(t.id) FILTER (WHERE t.status = 'in_progress') AS in_progress_tasks,
       COUNT(t.id) FILTER (WHERE t.status = 'blocked') AS blocked_tasks,
       COUNT(t.id) FILTER (WHERE t.status = 'closed') AS closed_tasks
FROM projects AS p
LEFT JOIN tasks AS t ON t.project_id = p.id
GROUP BY p.id, p.name
ORDER BY p.id;

-- Задание 4: choose_filter_vs_case
-- Кратко объясни FILTER vs CASE.
SELECT 'FILTER is usually clearer for compact pivot-like aggregates, while CASE is useful when the conditional logic itself must return a value.' AS note;

-- Задание 5: compact_dashboard_row
-- Собери одну компактную dashboard-строку на проект.
WITH task_status AS (
    SELECT project_id,
           COUNT(*) FILTER (WHERE status = 'open') AS open_tasks,
           COUNT(*) FILTER (WHERE status = 'in_progress') AS in_progress_tasks,
           COUNT(*) FILTER (WHERE status = 'blocked') AS blocked_tasks,
           COUNT(*) FILTER (WHERE status = 'closed') AS closed_tasks
    FROM tasks
    GROUP BY project_id
),
active_defects AS (
    SELECT t.project_id,
           COUNT(d.id) FILTER (WHERE d.status IN ('open', 'in_progress')) AS active_defects
    FROM tasks AS t
    LEFT JOIN defects AS d ON d.task_id = t.id
    GROUP BY t.project_id
)
SELECT p.name AS project_name,
       COALESCE(ts.open_tasks, 0) AS open_tasks,
       COALESCE(ts.in_progress_tasks, 0) AS in_progress_tasks,
       COALESCE(ts.blocked_tasks, 0) AS blocked_tasks,
       COALESCE(ts.closed_tasks, 0) AS closed_tasks,
       COALESCE(ad.active_defects, 0) AS active_defects
FROM projects AS p
LEFT JOIN task_status AS ts ON ts.project_id = p.id
LEFT JOIN active_defects AS ad ON ad.project_id = p.id
ORDER BY p.id;
