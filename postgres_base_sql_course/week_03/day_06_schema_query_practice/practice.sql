-- Практика: схема и запросы

-- Задание 1: non_owner_users
-- Верни имена пользователей, которые не владеют ни одним проектом.
-- expected: Oleg
SELECT 'TODO: non_owner_users' AS todo;

-- Задание 2: tasks_above_avg_points
-- Верни id задач с estimate_points выше среднего по tasks.
-- expected: 3
SELECT 'TODO: tasks_above_avg_points' AS todo;

-- Задание 3: projects_without_defects
-- Верни name проектов, где на задачах нет дефектов.
-- expected: Mobile App
SELECT 'TODO: projects_without_defects' AS todo;

-- Задание 4: not_null_columns_in_tasks
-- Верни имена NOT NULL колонок таблицы tasks через information_schema.
-- expected: id, project_id, assignee_id, status, priority, estimate_points
SELECT 'TODO: not_null_columns_in_tasks' AS todo;

-- Задание 5: foreign_key_count
-- Верни количество FOREIGN KEY constraints в таблицах public schema.
-- expected: 7
SELECT 'TODO: foreign_key_count' AS todo;
