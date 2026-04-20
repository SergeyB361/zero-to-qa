-- Практика: NULL, LIKE, ILIKE, IN, BETWEEN

-- Задание 1: open_ended_tasks
-- Верни id задач, у которых closed_at IS NULL.
-- expected: 1, 3, 4
SELECT id
FROM tasks
WHERE closed_at IS NULL
ORDER BY id;

-- Задание 2: login_related_defects
-- Верни title дефектов, где title содержит слово login без учёта регистра.
-- expected: Login 500
SELECT title
FROM defects
WHERE title ILIKE '%login%'
ORDER BY title;

-- Задание 3: active_web_or_api_users
-- Верни имена активных пользователей из команд web и api.
-- expected: Anna, Boris, Oleg
SELECT name
FROM users
WHERE is_active = TRUE
  AND team IN ('web', 'api')
ORDER BY name;

-- Задание 4: medium_duration_runs
-- Верни id test_runs, у которых duration_seconds BETWEEN 30 AND 50.
-- expected: 1, 2
SELECT id
FROM test_runs
WHERE duration_seconds BETWEEN 30 AND 50
ORDER BY id;

-- Задание 5: open_or_blocked_tasks
-- Верни id и status активных задач: open, in_progress или blocked.
-- expected: ids 1, 3, 4
SELECT id,
       status
FROM tasks
WHERE status IN ('open', 'in_progress', 'blocked')
ORDER BY id;
