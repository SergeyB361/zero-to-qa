-- Финальная практика по week 04

-- Задание 1: people_in_both_owner_and_reporter_roles
-- Верни имена пользователей, которые встречаются и как project owner, и как defect reporter.
-- expected: Anna, Boris
SELECT 'TODO: people_in_both_owner_and_reporter_roles' AS todo;

-- Задание 2: project_task_load
-- Верни project_name, total_tasks и unfinished_tasks.
-- expected:
-- Web Portal = total 2 / unfinished 1
-- Public API = total 1 / unfinished 1
-- Mobile App = total 1 / unfinished 1
SELECT 'TODO: project_task_load' AS todo;

-- Задание 3: daily_run_status_summary
-- Построй дневной summary по test_runs с total, passed, failed и blocked.
-- expected: 2026-04-10 -> total 4 / passed 2 / failed 1 / blocked 1
SELECT 'TODO: daily_run_status_summary' AS todo;

-- Задание 4: latest_executor_activity
-- Верни последний run по каждому executor.
-- expected: Anna -> 1, Boris -> 3, Oleg -> 4
SELECT 'TODO: latest_executor_activity' AS todo;

-- Задание 5: open_defect_titles_by_reporter
-- Для defects со статусами open/in_progress собери reporter -> STRING_AGG(title, ', ' ORDER BY title).
-- expected: Anna -> Login 500; Boris -> Refresh loop
SELECT 'TODO: open_defect_titles_by_reporter' AS todo;
