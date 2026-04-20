-- Практика: aggregate functions

-- Задание 1: total_users
-- Верни количество пользователей.
-- expected: 4
SELECT COUNT(*) AS total_users
FROM users;

-- Задание 2: open_defects_count
-- Верни количество дефектов со статусом open.
-- expected: 1
SELECT COUNT(*) AS open_defects_count
FROM defects
WHERE status = 'open';

-- Задание 3: avg_run_duration
-- Верни среднюю длительность test_runs.
-- expected: числовое значение > 0
SELECT ROUND(AVG(duration_seconds), 2) AS avg_run_duration
FROM test_runs;

-- Задание 4: min_max_task_points
-- Верни минимальное и максимальное estimate_points по tasks.
-- expected: 3 и 8
SELECT MIN(estimate_points) AS min_points,
       MAX(estimate_points) AS max_points
FROM tasks;

-- Задание 5: count_closed_timestamps
-- Верни количество строк tasks, где closed_at заполнен.
-- expected: 1
SELECT COUNT(closed_at) AS closed_timestamps_count
FROM tasks;
