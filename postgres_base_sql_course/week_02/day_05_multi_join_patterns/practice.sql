-- Практика: multi-join patterns

-- Задание 1: tasks_projects_owners
-- Верни task id, project name и project owner name.
-- expected: task 1 -> Web Portal -> Anna
SELECT t.id,
       p.name AS project_name,
       owner_user.name AS owner_name
FROM tasks AS t
JOIN projects AS p ON p.id = t.project_id
JOIN users AS owner_user ON owner_user.id = p.owner_id
ORDER BY t.id;

-- Задание 2: runs_cases_users
-- Верни run id, case title и executed_by_name.
-- expected: run 2 -> Create order -> Boris
SELECT r.id,
       c.title,
       u.name AS executed_by_name
FROM test_runs AS r
JOIN test_cases AS c ON c.id = r.case_id
JOIN users AS u ON u.id = r.executed_by
ORDER BY r.id;

-- Задание 3: defects_tasks_assignees
-- Верни defect title, task id и имя assignee связанной задачи.
-- expected: Login 500 -> task 2 -> Oleg
SELECT d.title,
       t.id AS task_id,
       u.name AS assignee_name
FROM defects AS d
JOIN tasks AS t ON t.id = d.task_id
JOIN users AS u ON u.id = t.assignee_id
ORDER BY d.id;

-- Задание 4: project_owner_and_active_flag
-- Верни project name, owner name и owner.is_active.
-- expected: Mobile App -> Nina -> false
SELECT p.name AS project_name,
       u.name AS owner_name,
       u.is_active
FROM projects AS p
JOIN users AS u ON u.id = p.owner_id
ORDER BY p.id;

-- Задание 5: task_case_style_report
-- Собери короткий отчёт по runs: run id, case title, user team.
-- expected: run 1 -> Login works -> web
SELECT r.id,
       c.title,
       u.team
FROM test_runs AS r
JOIN test_cases AS c ON c.id = r.case_id
JOIN users AS u ON u.id = r.executed_by
ORDER BY r.id;
