-- Практика: multi-join patterns

-- Задание 1: tasks_projects_owners
-- Верни task id, project name и project owner name.
-- expected: task 1 -> Web Portal -> Anna
SELECT 'TODO: tasks_projects_owners' AS todo;

-- Задание 2: runs_cases_users
-- Верни run id, case title и executed_by_name.
-- expected: run 2 -> Create order -> Boris
SELECT 'TODO: runs_cases_users' AS todo;

-- Задание 3: defects_tasks_assignees
-- Верни defect title, task id и имя assignee связанной задачи.
-- expected: Login 500 -> task 2 -> Oleg
SELECT 'TODO: defects_tasks_assignees' AS todo;

-- Задание 4: project_owner_and_active_flag
-- Верни project name, owner name и owner.is_active.
-- expected: Mobile App -> Nina -> false
SELECT 'TODO: project_owner_and_active_flag' AS todo;

-- Задание 5: task_case_style_report
-- Собери короткий отчёт по runs: run id, case title, user team.
-- expected: run 1 -> Login works -> web
SELECT 'TODO: task_case_style_report' AS todo;
