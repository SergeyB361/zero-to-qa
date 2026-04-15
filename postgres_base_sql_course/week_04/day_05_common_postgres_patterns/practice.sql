-- Практика: common Postgres patterns

-- Задание 1: run_status_summary_with_filter
-- Посчитай total, passed, failed и blocked test_runs через FILTER.
-- expected: total = 4, passed = 2, failed = 1, blocked = 1
SELECT 'TODO: run_status_summary_with_filter' AS todo;

-- Задание 2: latest_run_per_executor
-- Верни последний run по каждому executor через DISTINCT ON.
-- expected: Anna -> 1, Boris -> 3, Oleg -> 4
SELECT 'TODO: latest_run_per_executor' AS todo;

-- Задание 3: defect_titles_by_severity
-- Собери STRING_AGG(title, ', ' ORDER BY title) по severity.
-- expected: critical -> Login 500, Refresh loop; major -> Wrong total
SELECT 'TODO: defect_titles_by_severity' AS todo;

-- Задание 4: newest_user_per_team
-- Через DISTINCT ON верни самого нового пользователя в каждой team.
-- expected: api -> Boris, mobile -> Nina, web -> Oleg
SELECT 'TODO: newest_user_per_team' AS todo;

-- Задание 5: active_user_names_by_team
-- Для активных пользователей собери STRING_AGG(name, ', ' ORDER BY name) по team.
-- expected: api -> Boris; web -> Anna, Oleg
SELECT 'TODO: active_user_names_by_team' AS todo;
