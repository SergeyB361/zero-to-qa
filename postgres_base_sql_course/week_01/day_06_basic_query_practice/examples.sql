-- Практика на базовые запросы: примеры сборки условий

-- Пример 1: активные пользователи web-команды.
SELECT id, name, team
FROM users
WHERE is_active IS TRUE AND team = 'web'
ORDER BY name;

-- Пример 2: failed или blocked test runs с заметной длительностью.
SELECT id, status, duration_seconds
FROM test_runs
WHERE status IN ('failed', 'blocked')
  AND duration_seconds >= 10
ORDER BY duration_seconds DESC;

-- Пример 3: короткий отчёт по дефектам.
SELECT id,
       title,
       severity,
       COALESCE(task_id::text, 'no task') AS task_link
FROM defects
WHERE status <> 'closed'
ORDER BY reported_at DESC;
