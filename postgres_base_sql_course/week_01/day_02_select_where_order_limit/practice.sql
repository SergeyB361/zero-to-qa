-- Практика: SELECT, WHERE, ORDER BY, LIMIT

-- Задание 1: active_users
-- Верни имена активных пользователей в алфавитном порядке.
-- expected: Anna, Boris, Oleg
SELECT name
FROM users
WHERE is_active = TRUE
ORDER BY name;

-- Задание 2: top_unfinished_tasks
-- Верни id двух незакрытых задач с максимальным estimate_points.
-- expected: ids 3, 1
SELECT id,
       status,
       estimate_points
FROM tasks
WHERE status <> 'closed'
ORDER BY estimate_points DESC, id
LIMIT 2;

-- Задание 3: newest_projects
-- Верни id и name двух самых новых проектов по created_at.
-- expected: Mobile App, Public API
SELECT id,
       name,
       created_at
FROM projects
ORDER BY created_at DESC, id DESC
LIMIT 2;

-- Задание 4: critical_task
-- Верни id, status и estimate_points задачи с priority = critical.
-- expected: одна строка для task id = 3
SELECT id,
       status,
       estimate_points
FROM tasks
WHERE priority = 'critical';

-- Задание 5: shortest_test_runs
-- Верни id и duration_seconds двух самых коротких test runs.
-- expected: ids 4, 1
SELECT id,
       duration_seconds
FROM test_runs
ORDER BY duration_seconds ASC, id
LIMIT 2;
