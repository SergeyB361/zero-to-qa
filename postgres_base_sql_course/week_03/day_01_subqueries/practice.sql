-- Практика: подзапросы

-- Задание 1: project_owner_names
-- Верни имена пользователей, которые являются owners проектов.
-- expected: Anna, Boris, Nina
SELECT name
FROM users
WHERE id IN (
    SELECT owner_id
    FROM projects
)
ORDER BY name;

-- Задание 2: above_average_tasks
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

-- Задание 3: users_with_unfinished_tasks
-- Верни имена пользователей, у которых есть задачи со status <> closed.
-- expected: Anna, Boris, Nina
SELECT name
FROM users
WHERE id IN (
    SELECT assignee_id
    FROM tasks
    WHERE status <> 'closed'
)
ORDER BY name;

-- Задание 4: cases_run_by_boris
-- Верни title test_cases, которые запускал Boris.
-- expected: Create order, Refresh token
SELECT title
FROM test_cases
WHERE id IN (
    SELECT case_id
    FROM test_runs
    WHERE executed_by = (
        SELECT id
        FROM users
        WHERE name = 'Boris'
    )
)
ORDER BY title;

-- Задание 5: defects_in_boris_projects
-- Верни title defects, связанных с задачами проектов, где owner = Boris.
-- expected: Refresh loop
SELECT title
FROM defects
WHERE task_id IN (
    SELECT t.id
    FROM tasks AS t
    WHERE t.project_id IN (
        SELECT p.id
        FROM projects AS p
        WHERE p.owner_id = (
            SELECT id
            FROM users
            WHERE name = 'Boris'
        )
    )
)
ORDER BY title;
