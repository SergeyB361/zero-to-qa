-- Практика: GROUP BY и HAVING

-- Задание 1: runs_per_status
-- Верни status и COUNT(*) по test_runs.
-- expected: blocked = 1, failed = 1, passed = 2
SELECT status,
       COUNT(*) AS runs_count
FROM test_runs
GROUP BY status
ORDER BY status;

-- Задание 2: tasks_per_priority
-- Верни priority и количество задач по каждому priority.
-- expected: high = 2
SELECT priority,
       COUNT(*) AS tasks_count
FROM tasks
GROUP BY priority
ORDER BY priority;

-- Задание 3: avg_duration_per_user
-- Верни executed_by и AVG(duration_seconds) по test_runs.
-- expected: по пользователю 2 средняя длительность выше 40
SELECT executed_by,
       ROUND(AVG(duration_seconds), 2) AS avg_duration
FROM test_runs
GROUP BY executed_by
ORDER BY executed_by;

-- Задание 4: statuses_with_multiple_tasks
-- Верни status и COUNT(*) только для тех групп в tasks, где COUNT(*) > 1.
-- expected: результат пустой
SELECT status,
       COUNT(*) AS tasks_count
FROM tasks
GROUP BY status
HAVING COUNT(*) > 1
ORDER BY status;

-- Задание 5: defect_severity_with_open_items
-- Верни severity и COUNT(*) для defects, где status <> closed, сгруппируй по severity.
-- expected: critical = 2, major = 1
SELECT severity,
       COUNT(*) AS defects_count
FROM defects
WHERE status <> 'closed'
GROUP BY severity
ORDER BY severity;
