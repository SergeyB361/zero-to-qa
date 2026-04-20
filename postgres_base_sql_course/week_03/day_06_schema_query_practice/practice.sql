-- Практика: схема и запросы

-- Задание 1: non_owner_users
-- Верни имена пользователей, которые не владеют ни одним проектом.
-- expected: Oleg
SELECT name
FROM users
WHERE id NOT IN (
    SELECT owner_id
    FROM projects
)
ORDER BY name;

-- Задание 2: tasks_above_avg_points
-- Верни id задач с estimate_points выше среднего по tasks.
-- expected: 3
SELECT id,
       estimate_points
FROM tasks
WHERE estimate_points > (
    SELECT AVG(estimate_points)
    FROM tasks
)
ORDER BY id;

-- Задание 3: projects_without_defects
-- Верни name проектов, где на задачах нет дефектов.
-- expected: Mobile App
SELECT p.name
FROM projects AS p
WHERE NOT EXISTS (
    SELECT 1
    FROM tasks AS t
    JOIN defects AS d ON d.task_id = t.id
    WHERE t.project_id = p.id
)
ORDER BY p.name;

-- Задание 4: not_null_columns_in_tasks
-- Верни имена NOT NULL колонок таблицы tasks через information_schema.
-- expected: id, project_id, assignee_id, status, priority, estimate_points
SELECT column_name
FROM information_schema.columns
WHERE table_schema = 'public'
  AND table_name = 'tasks'
  AND is_nullable = 'NO'
ORDER BY ordinal_position;

-- Задание 5: foreign_key_count
-- Верни количество FOREIGN KEY constraints в таблицах public schema.
-- expected: 7
SELECT COUNT(*) AS foreign_key_count
FROM information_schema.table_constraints
WHERE table_schema = 'public'
  AND constraint_type = 'FOREIGN KEY';
