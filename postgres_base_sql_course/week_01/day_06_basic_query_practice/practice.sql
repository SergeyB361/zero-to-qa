-- Практика: базовые запросы

-- Задание 1: active_users_created_order
-- Верни id, name, created_at активных пользователей, отсортированных по created_at.
-- expected: Anna, Boris, Oleg
SELECT id,
       name,
       created_at
FROM users
WHERE is_active = TRUE
ORDER BY created_at, id;

-- Задание 2: biggest_unfinished_tasks
-- Верни id, status, estimate_points задач, которые не closed, по убыванию estimate_points.
-- expected: task 3 выше task 1 и task 4
SELECT id,
       status,
       estimate_points
FROM tasks
WHERE status <> 'closed'
ORDER BY estimate_points DESC, id;

-- Задание 3: long_runs
-- Верни id и status test_runs с duration_seconds >= 40 по убыванию duration_seconds.
-- expected: ids 3, 2
SELECT id,
       status,
       duration_seconds
FROM test_runs
WHERE duration_seconds >= 40
ORDER BY duration_seconds DESC, id;

-- Задание 4: critical_or_major_defects
-- Верни title и severity для defects с severity = critical или major.
-- expected: Login 500, Wrong total, Refresh loop
SELECT title,
       severity
FROM defects
WHERE severity IN ('critical', 'major')
ORDER BY id;

-- Задание 5: formatted_case_titles
-- Верни title AS case_title и UPPER(priority) AS priority_upper для test_cases, отсортируй по title.
-- expected: читаемый список test_cases с alias и upper priority
SELECT title AS case_title,
       UPPER(priority) AS priority_upper
FROM test_cases
ORDER BY title;
