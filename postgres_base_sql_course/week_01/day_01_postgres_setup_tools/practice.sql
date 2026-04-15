-- Практика: Postgres setup и инструменты
-- Выполняй задания в базе zero_to_qa из postgres_lab.

-- Задание 1: current_connection
-- Верни название базы и имя текущего пользователя.
-- expected: одна строка с db_name = zero_to_qa и db_user = postgres
SELECT 'TODO: current_connection' AS todo;

-- Задание 2: list_public_tables
-- Верни список таблиц схемы public в алфавитном порядке.
-- expected: defects, projects, tasks, test_cases, test_runs, users
SELECT 'TODO: list_public_tables' AS todo;

-- Задание 3: describe_tasks_columns
-- Верни имена колонок таблицы tasks и их data_type.
-- expected: id, project_id, assignee_id, status, priority, estimate_points, closed_at
SELECT 'TODO: describe_tasks_columns' AS todo;

-- Задание 4: row_counts
-- Верни количество строк в users, projects и tasks.
-- expected: users = 4, projects = 3, tasks = 4
SELECT 'TODO: row_counts' AS todo;

-- Задание 5: sample_test_cases
-- Верни первые три test_cases по id: id, title, priority.
-- expected: Login works, Create order, Refresh token
SELECT 'TODO: sample_test_cases' AS todo;
