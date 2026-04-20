-- Практика: set operations

-- Задание 1: owner_or_reporter_names
-- Верни уникальные имена пользователей, которые встречаются либо как project owner,
-- либо как defect reporter.
-- expected: Anna, Boris, Nina
SELECT name
FROM users
WHERE id IN (SELECT owner_id FROM projects)
UNION
SELECT name
FROM users
WHERE id IN (SELECT reported_by FROM defects)
ORDER BY name;

-- Задание 2: assignee_not_owner_names
-- Верни имена пользователей, которые назначены на tasks, но не являются owner проектов.
-- expected: Oleg
SELECT name
FROM users
WHERE id IN (SELECT assignee_id FROM tasks)
EXCEPT
SELECT name
FROM users
WHERE id IN (SELECT owner_id FROM projects)
ORDER BY name;

-- Задание 3: active_users_not_reporters
-- Верни активных пользователей, которые не репортили defects.
-- expected: Oleg
SELECT name
FROM users
WHERE is_active = TRUE
EXCEPT
SELECT u.name
FROM users AS u
JOIN defects AS d ON d.reported_by = u.id
ORDER BY name;

-- Задание 4: all_status_values_union
-- Собери единый список статусов из tasks.status и test_runs.status.
-- expected: blocked, closed, failed, in_progress, open, passed
SELECT status
FROM tasks
UNION
SELECT status
FROM test_runs
ORDER BY status;

-- Задание 5: owner_and_reporter_union_all_count
-- Посчитай количество строк в UNION ALL по owner names и reporter names.
-- expected: 6
SELECT COUNT(*) AS owner_and_reporter_rows
FROM (
    SELECT owner_id AS user_id FROM projects
    UNION ALL
    SELECT reported_by AS user_id FROM defects
) AS people;
