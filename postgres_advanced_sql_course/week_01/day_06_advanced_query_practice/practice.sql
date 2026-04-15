-- Практика на advanced querying

-- Задание 1: latest_run_per_executor_report
-- Через CTE + ROW_NUMBER() верни последний run по каждому executor.
-- expected: Anna -> 1, Boris -> 3, Oleg -> 4
SELECT 'TODO: latest_run_per_executor_report' AS todo;

-- Задание 2: defect_summary_with_window
-- Верни defects и defects_per_reporter через COUNT(*) OVER (PARTITION BY reported_by).
-- expected: Anna -> 1, Boris -> 2
SELECT 'TODO: defect_summary_with_window' AS todo;

-- Задание 3: recursive_run_calendar_report
-- Построй календарь 2026-04-09 .. 2026-04-11 и посчитай runs_count по дням.
-- expected: 0, 4, 0
SELECT 'TODO: recursive_run_calendar_report' AS todo;

-- Задание 4: project_points_rank_report
-- Через CTE агрегируй total_points по проектам и затем посчитай RANK().
-- expected: Web Portal = 8 rank 1; Public API = 8 rank 1; Mobile App = 5 rank 3
SELECT 'TODO: project_points_rank_report' AS todo;

-- Задание 5: running_duration_report
-- Верни run id и running total duration_seconds по executed_at.
-- expected: 35.00, 76.00, 131.00, 143.00
SELECT 'TODO: running_duration_report' AS todo;
