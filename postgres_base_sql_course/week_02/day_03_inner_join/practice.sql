-- Практика: INNER JOIN

-- Задание 1: tasks_with_assignees
-- Верни task id и имя assignee.
-- expected: 4 строки
SELECT t.id,
       u.name AS assignee_name
FROM tasks AS t
JOIN users AS u ON u.id = t.assignee_id
ORDER BY t.id;

-- Задание 2: tasks_with_projects
-- Верни task id и название project.
-- expected: у task 3 project_name = Public API
SELECT t.id,
       p.name AS project_name
FROM tasks AS t
JOIN projects AS p ON p.id = t.project_id
ORDER BY t.id;

-- Задание 3: runs_with_case_titles
-- Верни run id, title test case и status.
-- expected: run 2 связан с Create order
SELECT r.id,
       c.title,
       r.status
FROM test_runs AS r
JOIN test_cases AS c ON c.id = r.case_id
ORDER BY r.id;

-- Задание 4: defects_with_reporters
-- Верни defect title и имя пользователя, который reported_by.
-- expected: Login 500 reported by Anna
SELECT d.title,
       u.name AS reporter_name
FROM defects AS d
JOIN users AS u ON u.id = d.reported_by
ORDER BY d.id;

-- Задание 5: project_owners
-- Верни project name и имя owner.
-- expected: Web Portal -> Anna
SELECT p.name AS project_name,
       u.name AS owner_name
FROM projects AS p
JOIN users AS u ON u.id = p.owner_id
ORDER BY p.id;
