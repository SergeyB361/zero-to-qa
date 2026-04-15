-- Подзапросы

-- Пример 1: задачи с estimate_points выше среднего по таблице.
SELECT id, estimate_points
FROM tasks
WHERE estimate_points > (
    SELECT AVG(estimate_points)
    FROM tasks
)
ORDER BY estimate_points DESC;

-- Пример 2: пользователи, которые владеют проектами.
SELECT id, name
FROM users
WHERE id IN (
    SELECT owner_id
    FROM projects
)
ORDER BY id;

-- Пример 3: test cases, у которых были failed runs.
SELECT id, title
FROM test_cases
WHERE id IN (
    SELECT case_id
    FROM test_runs
    WHERE status = 'failed'
)
ORDER BY id;
