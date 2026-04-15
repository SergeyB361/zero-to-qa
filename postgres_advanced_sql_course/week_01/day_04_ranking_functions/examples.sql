-- Ranking functions

-- Пример 1: row number по runs по времени выполнения.
SELECT id,
       executed_at,
       ROW_NUMBER() OVER (ORDER BY executed_at DESC) AS run_row_number
FROM test_runs
ORDER BY executed_at DESC;

-- Пример 2: row number внутри каждого executor.
SELECT id,
       executed_by,
       executed_at,
       ROW_NUMBER() OVER (PARTITION BY executed_by ORDER BY executed_at DESC) AS executor_run_number
FROM test_runs
ORDER BY executed_by, executor_run_number;

-- Пример 3: rank и dense_rank по estimate_points.
SELECT id,
       estimate_points,
       RANK() OVER (ORDER BY estimate_points DESC) AS points_rank,
       DENSE_RANK() OVER (ORDER BY estimate_points DESC) AS points_dense_rank
FROM tasks
ORDER BY estimate_points DESC, id;
