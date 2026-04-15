-- SELECT, WHERE, ORDER BY, LIMIT

-- Пример 1: активные пользователи.
SELECT id, name, team
FROM users
WHERE is_active IS TRUE
ORDER BY name ASC;

-- Пример 2: две самые "тяжёлые" незакрытые задачи.
SELECT id, status, estimate_points
FROM tasks
WHERE status <> 'closed'
ORDER BY estimate_points DESC
LIMIT 2;

-- Пример 3: последние по времени test runs.
SELECT id, status, duration_seconds, executed_at
FROM test_runs
ORDER BY executed_at DESC
LIMIT 2;
