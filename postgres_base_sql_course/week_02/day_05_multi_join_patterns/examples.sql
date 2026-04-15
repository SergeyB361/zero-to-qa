-- Multi-join patterns

-- Пример 1: задача, проект и владелец проекта.
SELECT t.id,
       p.name AS project_name,
       owner.name AS project_owner
FROM tasks AS t
INNER JOIN projects AS p ON p.id = t.project_id
INNER JOIN users AS owner ON owner.id = p.owner_id
ORDER BY t.id;

-- Пример 2: test run, test case и исполнитель.
SELECT tr.id,
       tc.title,
       u.name AS executed_by_name,
       tr.status
FROM test_runs AS tr
INNER JOIN test_cases AS tc ON tc.id = tr.case_id
INNER JOIN users AS u ON u.id = tr.executed_by
ORDER BY tr.id;

-- Пример 3: defect, task и assignee задачи.
SELECT d.title AS defect_title,
       t.id AS task_id,
       assignee.name AS task_assignee
FROM defects AS d
LEFT JOIN tasks AS t ON t.id = d.task_id
LEFT JOIN users AS assignee ON assignee.id = t.assignee_id
ORDER BY d.id;
