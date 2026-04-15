-- Window functions

-- Пример 1: total_runs на каждой строке.
SELECT id,
       status,
       COUNT(*) OVER () AS total_runs
FROM test_runs
ORDER BY id;

-- Пример 2: средняя длительность по executor на каждой строке.
SELECT id,
       executed_by,
       duration_seconds,
       AVG(duration_seconds) OVER (PARTITION BY executed_by) AS avg_duration_by_executor
FROM test_runs
ORDER BY id;

-- Пример 3: total estimate_points по проекту на каждой строке tasks.
SELECT id,
       project_id,
       estimate_points,
       SUM(estimate_points) OVER (PARTITION BY project_id) AS total_points_by_project
FROM tasks
ORDER BY id;

-- Пример 4: defects per reporter на каждой строке.
SELECT id,
       reported_by,
       title,
       COUNT(*) OVER (PARTITION BY reported_by) AS defects_per_reporter
FROM defects
ORDER BY id;
