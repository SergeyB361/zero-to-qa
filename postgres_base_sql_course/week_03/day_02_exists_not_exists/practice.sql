-- Практика: EXISTS / NOT EXISTS

-- Задание 1: users_with_projects
-- Верни имена пользователей, у которых есть хотя бы один проект.
-- expected: Anna, Boris, Nina
SELECT u.name
FROM users AS u
WHERE EXISTS (
    SELECT 1
    FROM projects AS p
    WHERE p.owner_id = u.id
)
ORDER BY u.name;

-- Задание 2: projects_without_defects
-- Верни названия проектов, где на связанных задачах нет ни одного defect.
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

-- Задание 3: cases_without_failed_runs
-- Верни title test_cases, у которых нет ни одного failed run.
-- expected: Login works, Refresh token, Profile update
SELECT c.title
FROM test_cases AS c
WHERE NOT EXISTS (
    SELECT 1
    FROM test_runs AS r
    WHERE r.case_id = c.id
      AND r.status = 'failed'
)
ORDER BY c.id;

-- Задание 4: tasks_with_defects
-- Верни id задач, у которых есть хотя бы один defect.
-- expected: 1, 2, 3
SELECT t.id
FROM tasks AS t
WHERE EXISTS (
    SELECT 1
    FROM defects AS d
    WHERE d.task_id = t.id
)
ORDER BY t.id;

-- Задание 5: users_without_reported_defects
-- Верни имена пользователей, которые не reported ни одного defect.
-- expected: Nina, Oleg
SELECT u.name
FROM users AS u
WHERE NOT EXISTS (
    SELECT 1
    FROM defects AS d
    WHERE d.reported_by = u.id
)
ORDER BY u.name;
