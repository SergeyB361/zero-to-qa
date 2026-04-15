-- DISTINCT, aliases, базовые функции

-- Пример 1: уникальные команды.
SELECT DISTINCT team
FROM users
ORDER BY team;

-- Пример 2: читаемые aliases.
SELECT name AS user_name,
       team AS squad,
       is_active AS active_flag
FROM users
ORDER BY user_name;

-- Пример 3: базовые функции для строк.
SELECT title,
       LENGTH(title) AS title_len,
       UPPER(area) AS area_upper
FROM test_cases
ORDER BY title;

-- Пример 4: COALESCE для работы с NULL.
SELECT id,
       status,
       COALESCE(closed_at::text, 'not closed yet') AS closed_info
FROM tasks
ORDER BY id;
