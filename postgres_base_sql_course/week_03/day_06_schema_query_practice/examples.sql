-- Практика на схему и запросы

-- Пример 1: список NOT NULL колонок в таблице defects.
SELECT column_name
FROM information_schema.columns
WHERE table_schema = 'public'
  AND table_name = 'defects'
  AND is_nullable = 'NO'
ORDER BY ordinal_position;

-- Пример 2: пользователи, которые не являются owners проектов.
SELECT name
FROM users
WHERE id NOT IN (
    SELECT owner_id
    FROM projects
)
ORDER BY name;

-- Пример 3: проекты, у которых есть defects на задачах.
SELECT p.name
FROM projects AS p
WHERE EXISTS (
    SELECT 1
    FROM tasks AS t
    JOIN defects AS d ON d.task_id = t.id
    WHERE t.project_id = p.id
)
ORDER BY p.name;
