-- Практика: set operations

-- Задание 1: owner_or_reporter_names
-- Верни уникальные имена пользователей, которые встречаются либо как project owner,
-- либо как defect reporter.
-- expected: Anna, Boris, Nina
SELECT 'TODO: owner_or_reporter_names' AS todo;

-- Задание 2: assignee_not_owner_names
-- Верни имена пользователей, которые назначены на tasks, но не являются owner проектов.
-- expected: Oleg
SELECT 'TODO: assignee_not_owner_names' AS todo;

-- Задание 3: active_users_not_reporters
-- Верни активных пользователей, которые не репортили defects.
-- expected: Oleg
SELECT 'TODO: active_users_not_reporters' AS todo;

-- Задание 4: all_status_values_union
-- Собери единый список статусов из tasks.status и test_runs.status.
-- expected: blocked, closed, failed, in_progress, open, passed
SELECT 'TODO: all_status_values_union' AS todo;

-- Задание 5: owner_and_reporter_union_all_count
-- Посчитай количество строк в UNION ALL по owner names и reporter names.
-- expected: 6
SELECT 'TODO: owner_and_reporter_union_all_count' AS todo;
