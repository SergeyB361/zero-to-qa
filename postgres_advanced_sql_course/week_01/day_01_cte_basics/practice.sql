-- Практика: CTE basics

-- Задание 1: unfinished_task_ids
-- Через CTE верни id всех задач со статусом не closed.
-- expected: 1, 3, 4
SELECT 'TODO: unfinished_task_ids' AS todo;

-- Задание 2: defect_counts_by_reporter
-- Через CTE посчитай количество defects по reporter.
-- expected: Anna = 1, Boris = 2
SELECT 'TODO: defect_counts_by_reporter' AS todo;

-- Задание 3: project_task_load_with_cte
-- Через CTE посчитай total_tasks и unfinished_tasks по проектам.
-- expected:
-- Web Portal = total 2 / unfinished 1
-- Public API = total 1 / unfinished 1
-- Mobile App = total 1 / unfinished 1
SELECT 'TODO: project_task_load_with_cte' AS todo;

-- Задание 4: avg_run_duration_by_executor_cte
-- Через CTE верни среднюю длительность test_runs по executor.
-- expected: Anna = 35.00, Boris = 48.00, Oleg = 12.00
SELECT 'TODO: avg_run_duration_by_executor_cte' AS todo;

-- Задание 5: defects_on_unfinished_tasks
-- Через CTE верни названия defects, связанных с задачами не closed.
-- expected: Refresh loop, Wrong total
SELECT 'TODO: defects_on_unfinished_tasks' AS todo;
