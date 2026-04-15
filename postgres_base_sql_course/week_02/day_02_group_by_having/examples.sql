-- GROUP BY и HAVING

-- Пример 1: число test_runs по статусу.
SELECT status, COUNT(*) AS total_runs
FROM test_runs
GROUP BY status
ORDER BY status;

-- Пример 2: средняя длительность по исполнителю.
SELECT executed_by, AVG(duration_seconds) AS avg_duration
FROM test_runs
GROUP BY executed_by
ORDER BY executed_by;

-- Пример 3: только те приоритеты задач, где больше одной строки.
SELECT priority, COUNT(*) AS total_tasks
FROM tasks
GROUP BY priority
HAVING COUNT(*) > 1
ORDER BY priority;
