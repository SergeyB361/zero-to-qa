-- Практика: DISTINCT, aliases, базовые функции

-- Задание 1: unique_teams
-- Верни уникальные team в алфавитном порядке.
-- expected: api, mobile, web
SELECT 'TODO: unique_teams' AS todo;

-- Задание 2: renamed_user_columns
-- Верни name AS user_name и team AS squad для всех пользователей.
-- expected: колонки user_name и squad
SELECT 'TODO: renamed_user_columns' AS todo;

-- Задание 3: case_title_lengths
-- Верни title и LENGTH(title) AS title_len для всех test_cases.
-- expected: у каждой строки есть title_len
SELECT 'TODO: case_title_lengths' AS todo;

-- Задание 4: uppercase_priorities
-- Верни title и UPPER(priority) AS priority_upper для test_cases.
-- expected: HIGH, CRITICAL, MEDIUM
SELECT 'TODO: uppercase_priorities' AS todo;

-- Задание 5: closed_info
-- Верни id и COALESCE(closed_at::text, 'not closed') AS closed_info для tasks.
-- expected: у открытых строк будет not closed
SELECT 'TODO: closed_info' AS todo;
