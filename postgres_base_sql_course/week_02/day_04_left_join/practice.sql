-- Практика: LEFT JOIN

-- Задание 1: test_cases_with_possible_runs
-- Верни title test case и run id, если запуск есть.
-- expected: Profile update будет с run id 4
SELECT c.title,
       r.id AS run_id
FROM test_cases AS c
LEFT JOIN test_runs AS r ON r.case_id = c.id
ORDER BY c.id, r.id;

-- Задание 2: defects_with_optional_task
-- Верни defect title и task id, даже если task отсутствует.
-- expected: все 3 defects остаются в результате
SELECT d.title,
       t.id AS task_id
FROM defects AS d
LEFT JOIN tasks AS t ON t.id = d.task_id
ORDER BY d.id;

-- Задание 3: find_cases_without_runs
-- Верни title test_cases, у которых нет ни одного test_run.
-- expected: результат пустой на текущем dataset
SELECT c.title
FROM test_cases AS c
LEFT JOIN test_runs AS r ON r.case_id = c.id
WHERE r.id IS NULL
ORDER BY c.title;

-- Задание 4: projects_with_task_count_basis
-- Верни project name и task id через LEFT JOIN.
-- expected: все 3 проекта присутствуют
SELECT p.name AS project_name,
       t.id AS task_id
FROM projects AS p
LEFT JOIN tasks AS t ON t.project_id = p.id
ORDER BY p.id, t.id;

-- Задание 5: tasks_with_possible_closed_at
-- Верни все tasks и связанный project name.
-- expected: 4 строки
SELECT t.id,
       t.closed_at,
       p.name AS project_name
FROM tasks AS t
LEFT JOIN projects AS p ON p.id = t.project_id
ORDER BY t.id;
