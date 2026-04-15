-- Практика: NULL, LIKE, ILIKE, IN, BETWEEN

-- Задание 1: open_ended_tasks
-- Верни id задач, у которых closed_at IS NULL.
-- expected: 1, 3, 4
SELECT 'TODO: open_ended_tasks' AS todo;

-- Задание 2: login_related_defects
-- Верни title дефектов, где title содержит слово login без учёта регистра.
-- expected: Login 500
SELECT 'TODO: login_related_defects' AS todo;

-- Задание 3: active_web_or_api_users
-- Верни имена активных пользователей из команд web и api.
-- expected: Anna, Boris, Oleg
SELECT 'TODO: active_web_or_api_users' AS todo;

-- Задание 4: medium_duration_runs
-- Верни id test_runs, у которых duration_seconds BETWEEN 30 AND 50.
-- expected: 1, 2
SELECT 'TODO: medium_duration_runs' AS todo;

-- Задание 5: open_or_blocked_tasks
-- Верни id и status задач со статусом open или blocked.
-- expected: ids 1 и 4
SELECT 'TODO: open_or_blocked_tasks' AS todo;
