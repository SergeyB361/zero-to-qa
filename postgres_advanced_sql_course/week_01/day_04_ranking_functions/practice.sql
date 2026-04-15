-- Практика: ranking functions

-- Задание 1: global_duration_row_number
-- Верни test_runs в порядке duration_seconds DESC и посчитай ROW_NUMBER().
-- expected: id 3 -> 1, id 2 -> 2, id 1 -> 3, id 4 -> 4
SELECT 'TODO: global_duration_row_number' AS todo;

-- Задание 2: per_executor_row_number
-- Верни ROW_NUMBER() по каждому executor по executed_at DESC.
-- expected: для Boris id 3 -> 1, id 2 -> 2
SELECT 'TODO: per_executor_row_number' AS todo;

-- Задание 3: task_points_rank
-- Посчитай RANK() по estimate_points DESC.
-- expected: id 3 -> rank 1, id 1 -> rank 2, id 4 -> rank 2, id 2 -> rank 4
SELECT 'TODO: task_points_rank' AS todo;

-- Задание 4: task_points_dense_rank
-- Посчитай DENSE_RANK() по estimate_points DESC.
-- expected: id 3 -> dense_rank 1, id 1 -> 2, id 4 -> 2, id 2 -> 3
SELECT 'TODO: task_points_dense_rank' AS todo;

-- Задание 5: latest_run_per_executor_with_row_number
-- Через CTE и ROW_NUMBER() верни последний run по каждому executor.
-- expected: Anna -> 1, Boris -> 3, Oleg -> 4
SELECT 'TODO: latest_run_per_executor_with_row_number' AS todo;
