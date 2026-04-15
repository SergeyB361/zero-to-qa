-- INNER JOIN

-- Пример 1: задачи и имена исполнителей.
SELECT t.id, t.status, u.name AS assignee_name
FROM tasks AS t
INNER JOIN users AS u ON t.assignee_id = u.id
ORDER BY t.id;

-- Пример 2: задачи и проекты.
SELECT t.id, p.name AS project_name, t.priority
FROM tasks AS t
INNER JOIN projects AS p ON t.project_id = p.id
ORDER BY t.id;

-- Пример 3: test runs и названия test cases.
SELECT tr.id, tc.title, tr.status, tr.duration_seconds
FROM test_runs AS tr
INNER JOIN test_cases AS tc ON tr.case_id = tc.id
ORDER BY tr.id;
