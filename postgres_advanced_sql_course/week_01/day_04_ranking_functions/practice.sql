-- Практика: ranking functions

-- Задание 1: global_duration_row_number
-- Верни test_runs в порядке duration_seconds DESC и посчитай ROW_NUMBER().
-- expected: id 3 -> 1, id 2 -> 2, id 1 -> 3, id 4 -> 4
SELECT id,
       duration_seconds,
       ROW_NUMBER() OVER (ORDER BY duration_seconds DESC, id) AS rn
FROM test_runs
ORDER BY rn;

-- Задание 2: per_executor_row_number
-- Верни ROW_NUMBER() по каждому executor по executed_at DESC.
-- expected: для Boris id 3 -> 1, id 2 -> 2
SELECT id,
       executed_by,
       executed_at,
       ROW_NUMBER() OVER (PARTITION BY executed_by ORDER BY executed_at DESC, id DESC) AS rn
FROM test_runs
ORDER BY executed_by, rn;

-- Задание 3: task_points_rank
-- Посчитай RANK() по estimate_points DESC.
-- expected: id 3 -> rank 1, id 1 -> rank 2, id 4 -> rank 2, id 2 -> rank 4
SELECT id,
       estimate_points,
       RANK() OVER (ORDER BY estimate_points DESC) AS rank_value
FROM tasks
ORDER BY id;

-- Задание 4: task_points_dense_rank
-- Посчитай DENSE_RANK() по estimate_points DESC.
-- expected: id 3 -> dense_rank 1, id 1 -> 2, id 4 -> 2, id 2 -> 3
SELECT id,
       estimate_points,
       DENSE_RANK() OVER (ORDER BY estimate_points DESC) AS dense_rank_value
FROM tasks
ORDER BY id;

-- Задание 5: latest_run_per_executor_with_row_number
-- Через CTE и ROW_NUMBER() верни последний run по каждому executor.
-- expected: Anna -> 1, Boris -> 3, Oleg -> 4
WITH ranked_runs AS (
    SELECT r.id,
           r.executed_by,
           ROW_NUMBER() OVER (PARTITION BY r.executed_by ORDER BY r.executed_at DESC, r.id DESC) AS rn
    FROM test_runs AS r
)
SELECT u.name,
       rr.id AS latest_run_id
FROM ranked_runs AS rr
JOIN users AS u ON u.id = rr.executed_by
WHERE rr.rn = 1
ORDER BY u.name;
