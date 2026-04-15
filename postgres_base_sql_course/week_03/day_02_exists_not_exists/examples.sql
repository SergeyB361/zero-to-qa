-- EXISTS / NOT EXISTS

-- Пример 1: пользователи, у которых есть проекты.
SELECT u.id, u.name
FROM users AS u
WHERE EXISTS (
    SELECT 1
    FROM projects AS p
    WHERE p.owner_id = u.id
)
ORDER BY u.id;

-- Пример 2: проекты, у которых нет ни одного defect на их задачах.
SELECT p.id, p.name
FROM projects AS p
WHERE NOT EXISTS (
    SELECT 1
    FROM tasks AS t
    JOIN defects AS d ON d.task_id = t.id
    WHERE t.project_id = p.id
)
ORDER BY p.id;

-- Пример 3: test cases, у которых есть failed run.
SELECT tc.id, tc.title
FROM test_cases AS tc
WHERE EXISTS (
    SELECT 1
    FROM test_runs AS tr
    WHERE tr.case_id = tc.id AND tr.status = 'failed'
)
ORDER BY tc.id;
