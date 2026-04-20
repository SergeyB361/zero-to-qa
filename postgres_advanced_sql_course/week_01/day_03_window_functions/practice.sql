-- Практика: window functions

-- Задание 1: total_runs_on_each_row
-- Верни id, status и COUNT(*) OVER () для test_runs.
-- expected: total_runs = 4 на каждой строке
SELECT id,
       status,
       COUNT(*) OVER () AS total_runs
FROM test_runs
ORDER BY id;

-- Задание 2: avg_duration_per_executor_window
-- Верни id, executed_by и AVG(duration_seconds) OVER (PARTITION BY executed_by).
-- expected: Anna = 35.00, Boris = 48.00, Oleg = 12.00
SELECT id,
       executed_by,
       ROUND(AVG(duration_seconds) OVER (PARTITION BY executed_by), 2) AS avg_duration_per_executor
FROM test_runs
ORDER BY id;

-- Задание 3: project_total_points_window
-- Верни tasks с total_points_by_project через SUM(...) OVER (PARTITION BY project_id).
-- expected: project 1 -> 8, project 2 -> 8, project 3 -> 5
SELECT id,
       project_id,
       estimate_points,
       SUM(estimate_points) OVER (PARTITION BY project_id) AS total_points_by_project
FROM tasks
ORDER BY id;

-- Задание 4: defects_per_reporter_window
-- Верни defects с COUNT(*) OVER (PARTITION BY reported_by).
-- expected: reported_by = 1 -> 1, reported_by = 2 -> 2
SELECT id,
       title,
       reported_by,
       COUNT(*) OVER (PARTITION BY reported_by) AS defects_per_reporter
FROM defects
ORDER BY id;

-- Задание 5: unfinished_tasks_per_project_window
-- Верни tasks и COUNT(*) FILTER (WHERE status <> 'closed') OVER (PARTITION BY project_id).
-- expected: для project 1 значение unfinished = 1, для project 2 = 1, для project 3 = 1
SELECT id,
       project_id,
       status,
       COUNT(*) FILTER (WHERE status <> 'closed') OVER (PARTITION BY project_id) AS unfinished_tasks_per_project
FROM tasks
ORDER BY id;
