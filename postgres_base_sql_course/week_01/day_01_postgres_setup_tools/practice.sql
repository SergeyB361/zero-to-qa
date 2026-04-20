-- Практика: Postgres setup и инструменты
-- Выполняй задания в базе zero_to_qa из postgres_lab.

-- Задание 1: current_connection
-- Верни название базы и имя текущего пользователя.
-- expected: одна строка с db_name = zero_to_qa и db_user = postgres
SELECT current_database() AS db_name,
       current_user AS db_user;

-- Задание 2: list_public_tables
-- Верни список таблиц схемы public в алфавитном порядке.
-- expected: defects, projects, tasks, test_cases, test_runs, users
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
ORDER BY table_name;

-- Задание 3: describe_tasks_columns
-- Верни имена колонок таблицы tasks и их data_type.
-- expected: id, project_id, assignee_id, status, priority, estimate_points, closed_at
SELECT column_name,
       data_type
FROM information_schema.columns
WHERE table_schema = 'public'
  AND table_name = 'tasks'
ORDER BY ordinal_position;

-- Задание 4: row_counts
-- Верни количество строк в users, projects и tasks.
-- expected: users = 4, projects = 3, tasks = 4
SELECT 'users' AS table_name, COUNT(*) AS row_count FROM users
UNION ALL
SELECT 'projects' AS table_name, COUNT(*) AS row_count FROM projects
UNION ALL
SELECT 'tasks' AS table_name, COUNT(*) AS row_count FROM tasks
ORDER BY table_name;

-- Задание 5: sample_test_cases
-- Верни первые три test_cases по id: id, title, priority.
-- expected: Login works, Create order, Refresh token
SELECT id,
       title,
       priority
FROM test_cases
ORDER BY id
LIMIT 3;
