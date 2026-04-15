-- Практика: SELECT, WHERE, ORDER BY, LIMIT

-- Задание 1: active_users
-- Верни имена активных пользователей в алфавитном порядке.
-- expected: Anna, Boris, Oleg
SELECT 'TODO: active_users' AS todo;

-- Задание 2: top_unfinished_tasks
-- Верни id двух незакрытых задач с максимальным estimate_points.
-- expected: ids 3, 1
SELECT 'TODO: top_unfinished_tasks' AS todo;

-- Задание 3: newest_projects
-- Верни id и name двух самых новых проектов по created_at.
-- expected: Mobile App, Public API
SELECT 'TODO: newest_projects' AS todo;

-- Задание 4: critical_task
-- Верни id, status и estimate_points задачи с priority = critical.
-- expected: одна строка для task id = 3
SELECT 'TODO: critical_task' AS todo;

-- Задание 5: shortest_test_runs
-- Верни id и duration_seconds двух самых коротких test runs.
-- expected: ids 4, 1
SELECT 'TODO: shortest_test_runs' AS todo;
