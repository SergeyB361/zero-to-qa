-- Практика: DISTINCT, aliases, базовые функции

-- Задание 1: unique_teams
-- Верни уникальные team в алфавитном порядке.
-- expected: api, mobile, web
SELECT DISTINCT team
FROM users
ORDER BY team;

-- Задание 2: renamed_user_columns
-- Верни name AS user_name и team AS squad для всех пользователей.
-- expected: колонки user_name и squad
SELECT name AS user_name,
       team AS squad
FROM users
ORDER BY id;

-- Задание 3: case_title_lengths
-- Верни title и LENGTH(title) AS title_len для всех test_cases.
-- expected: у каждой строки есть title_len
SELECT title,
       LENGTH(title) AS title_len
FROM test_cases
ORDER BY id;

-- Задание 4: uppercase_priorities
-- Верни title и UPPER(priority) AS priority_upper для test_cases.
-- expected: HIGH, CRITICAL, MEDIUM
SELECT title,
       UPPER(priority) AS priority_upper
FROM test_cases
ORDER BY id;

-- Задание 5: closed_info
-- Верни id и COALESCE(closed_at::text, 'not closed') AS closed_info для tasks.
-- expected: у открытых строк будет not closed
SELECT id,
       COALESCE(closed_at::text, 'not closed') AS closed_info
FROM tasks
ORDER BY id;
