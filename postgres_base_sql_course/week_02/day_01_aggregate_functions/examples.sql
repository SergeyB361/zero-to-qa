-- Aggregate functions

-- Пример 1: сколько задач не закрыто.
SELECT COUNT(*) AS unfinished_tasks
FROM tasks
WHERE status <> 'closed';

-- Пример 2: средняя длительность test run.
SELECT AVG(duration_seconds) AS avg_run_duration
FROM test_runs;

-- Пример 3: минимальная и максимальная оценка задач.
SELECT MIN(estimate_points) AS min_points,
       MAX(estimate_points) AS max_points
FROM tasks;

-- Пример 4: сколько задач уже имеют closed_at.
SELECT COUNT(closed_at) AS closed_tasks_with_timestamp
FROM tasks;
