-- Практика: LEFT JOIN

-- Задание 1: test_cases_with_possible_runs
-- Верни title test case и run id, если запуск есть.
-- expected: Profile update будет с run id 4
SELECT 'TODO: test_cases_with_possible_runs' AS todo;

-- Задание 2: defects_with_optional_task
-- Верни defect title и task id, даже если task отсутствует.
-- expected: все 3 defects остаются в результате
SELECT 'TODO: defects_with_optional_task' AS todo;

-- Задание 3: find_cases_without_runs
-- Верни title test_cases, у которых нет ни одного test_run.
-- expected: результат пустой на текущем dataset
SELECT 'TODO: find_cases_without_runs' AS todo;

-- Задание 4: projects_with_task_count_basis
-- Верни project name и task id через LEFT JOIN.
-- expected: все 3 проекта присутствуют
SELECT 'TODO: projects_with_task_count_basis' AS todo;

-- Задание 5: tasks_with_possible_closed_at
-- Верни все tasks и связанный project name.
-- expected: 4 строки
SELECT 'TODO: tasks_with_possible_closed_at' AS todo;
