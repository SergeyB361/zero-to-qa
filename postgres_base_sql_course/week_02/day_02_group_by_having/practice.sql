-- Практика: GROUP BY и HAVING

-- Задание 1: runs_per_status
-- Верни status и COUNT(*) по test_runs.
-- expected: blocked = 1, failed = 1, passed = 2
SELECT 'TODO: runs_per_status' AS todo;

-- Задание 2: tasks_per_priority
-- Верни priority и количество задач по каждому priority.
-- expected: high = 2
SELECT 'TODO: tasks_per_priority' AS todo;

-- Задание 3: avg_duration_per_user
-- Верни executed_by и AVG(duration_seconds) по test_runs.
-- expected: по пользователю 2 средняя длительность выше 40
SELECT 'TODO: avg_duration_per_user' AS todo;

-- Задание 4: statuses_with_multiple_tasks
-- Верни status и COUNT(*) только для тех групп в tasks, где COUNT(*) > 1.
-- expected: open = 1? нет, open = 1, closed = 1, in_progress = 1, blocked = 1; результат пустой
SELECT 'TODO: statuses_with_multiple_tasks' AS todo;

-- Задание 5: defect_severity_with_open_items
-- Верни severity и COUNT(*) для defects, где status <> closed, сгруппируй по severity.
-- expected: critical = 2, major = 1
SELECT 'TODO: defect_severity_with_open_items' AS todo;
