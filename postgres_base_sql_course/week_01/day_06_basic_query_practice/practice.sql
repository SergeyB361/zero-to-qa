-- Практика: базовые запросы

-- Задание 1: active_users_created_order
-- Верни id, name, created_at активных пользователей, отсортированных по created_at.
-- expected: Anna, Boris, Oleg
SELECT 'TODO: active_users_created_order' AS todo;

-- Задание 2: biggest_unfinished_tasks
-- Верни id, status, estimate_points задач, которые не closed, по убыванию estimate_points.
-- expected: task 3 выше task 1 и task 4
SELECT 'TODO: biggest_unfinished_tasks' AS todo;

-- Задание 3: long_runs
-- Верни id и status test_runs с duration_seconds >= 40 по убыванию duration_seconds.
-- expected: ids 3, 2
SELECT 'TODO: long_runs' AS todo;

-- Задание 4: critical_or_major_defects
-- Верни title и severity для defects с severity = critical или major.
-- expected: Login 500, Wrong total, Refresh loop
SELECT 'TODO: critical_or_major_defects' AS todo;

-- Задание 5: formatted_case_titles
-- Верни title AS case_title и UPPER(priority) AS priority_upper для test_cases, отсортируй по title.
-- expected: читаемый список test_cases с alias и upper priority
SELECT 'TODO: formatted_case_titles' AS todo;
