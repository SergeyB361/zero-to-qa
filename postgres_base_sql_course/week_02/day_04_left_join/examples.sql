-- LEFT JOIN

-- Пример 1: все test cases и их test runs, если они есть.
SELECT tc.id, tc.title, tr.id AS run_id, tr.status
FROM test_cases AS tc
LEFT JOIN test_runs AS tr ON tr.case_id = tc.id
ORDER BY tc.id, tr.id;

-- Пример 2: все defects и связанные task, если task есть.
SELECT d.id, d.title, t.id AS task_id, t.status AS task_status
FROM defects AS d
LEFT JOIN tasks AS t ON d.task_id = t.id
ORDER BY d.id;

-- Пример 3: projects и задачи, если задачи есть.
SELECT p.id, p.name, t.id AS task_id
FROM projects AS p
LEFT JOIN tasks AS t ON t.project_id = p.id
ORDER BY p.id, t.id;
