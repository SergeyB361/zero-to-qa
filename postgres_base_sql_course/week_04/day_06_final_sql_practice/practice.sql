-- Финальная практика по week 04

-- Задание 1: people_in_both_owner_and_reporter_roles
-- Верни имена пользователей, которые встречаются и как project owner, и как defect reporter.
-- expected: Anna, Boris
SELECT name
FROM users
WHERE id IN (SELECT owner_id FROM projects)
INTERSECT
SELECT name
FROM users
WHERE id IN (SELECT reported_by FROM defects)
ORDER BY name;

-- Задание 2: project_task_load
-- Верни project_name, total_tasks и unfinished_tasks.
-- expected:
-- Web Portal = total 2 / unfinished 1
-- Public API = total 1 / unfinished 1
-- Mobile App = total 1 / unfinished 1
SELECT p.name AS project_name,
       COUNT(t.id) AS total_tasks,
       COUNT(*) FILTER (WHERE t.status <> 'closed') AS unfinished_tasks
FROM projects AS p
LEFT JOIN tasks AS t ON t.project_id = p.id
GROUP BY p.id, p.name
ORDER BY p.id;

-- Задание 3: daily_run_status_summary
-- Построй дневной summary по test_runs с total, passed, failed и blocked.
-- expected: 2026-04-10 -> total 4 / passed 2 / failed 1 / blocked 1
SELECT (executed_at AT TIME ZONE 'Europe/Moscow')::date AS run_day,
       COUNT(*) AS total_runs,
       COUNT(*) FILTER (WHERE status = 'passed') AS passed_runs,
       COUNT(*) FILTER (WHERE status = 'failed') AS failed_runs,
       COUNT(*) FILTER (WHERE status = 'blocked') AS blocked_runs
FROM test_runs
GROUP BY run_day
ORDER BY run_day;

-- Задание 4: latest_executor_activity
-- Верни последний run по каждому executor.
-- expected: Anna -> 1, Boris -> 3, Oleg -> 4
SELECT DISTINCT ON (u.id)
       u.name,
       r.id AS latest_run_id,
       r.executed_at
FROM test_runs AS r
JOIN users AS u ON u.id = r.executed_by
ORDER BY u.id, r.executed_at DESC, r.id DESC;

-- Задание 5: open_defect_titles_by_reporter
-- Для defects со статусами open/in_progress собери reporter -> STRING_AGG(title, ', ' ORDER BY title).
-- expected: Anna -> Login 500; Boris -> Refresh loop
SELECT u.name AS reporter_name,
       STRING_AGG(d.title, ', ' ORDER BY d.title) AS open_defect_titles
FROM defects AS d
JOIN users AS u ON u.id = d.reported_by
WHERE d.status IN ('open', 'in_progress')
GROUP BY u.id, u.name
ORDER BY u.name;
