-- Практика: CTE basics

-- Задание 1: unfinished_task_ids
-- Через CTE верни id всех задач со статусом не closed.
-- expected: 1, 3, 4
WITH unfinished_tasks AS (
    SELECT id
    FROM tasks
    WHERE status <> 'closed'
)
SELECT id
FROM unfinished_tasks
ORDER BY id;

-- Задание 2: defect_counts_by_reporter
-- Через CTE посчитай количество defects по reporter.
-- expected: Anna = 1, Boris = 2
WITH reporter_defects AS (
    SELECT reported_by,
           COUNT(*) AS defects_count
    FROM defects
    GROUP BY reported_by
)
SELECT u.name,
       rd.defects_count
FROM reporter_defects AS rd
JOIN users AS u ON u.id = rd.reported_by
ORDER BY u.name;

-- Задание 3: project_task_load_with_cte
-- Через CTE посчитай total_tasks и unfinished_tasks по проектам.
-- expected:
-- Web Portal = total 2 / unfinished 1
-- Public API = total 1 / unfinished 1
-- Mobile App = total 1 / unfinished 1
WITH project_load AS (
    SELECT project_id,
           COUNT(*) AS total_tasks,
           COUNT(*) FILTER (WHERE status <> 'closed') AS unfinished_tasks
    FROM tasks
    GROUP BY project_id
)
SELECT p.name,
       pl.total_tasks,
       pl.unfinished_tasks
FROM project_load AS pl
JOIN projects AS p ON p.id = pl.project_id
ORDER BY p.id;

-- Задание 4: avg_run_duration_by_executor_cte
-- Через CTE верни среднюю длительность test_runs по executor.
-- expected: Anna = 35.00, Boris = 48.00, Oleg = 12.00
WITH executor_runs AS (
    SELECT executed_by,
           AVG(duration_seconds) AS avg_duration
    FROM test_runs
    GROUP BY executed_by
)
SELECT u.name,
       ROUND(er.avg_duration, 2) AS avg_duration
FROM executor_runs AS er
JOIN users AS u ON u.id = er.executed_by
ORDER BY u.name;

-- Задание 5: defects_on_unfinished_tasks
-- Через CTE верни названия defects, связанных с задачами не closed.
-- expected: Refresh loop, Wrong total
WITH unfinished_tasks AS (
    SELECT id
    FROM tasks
    WHERE status <> 'closed'
)
SELECT d.title
FROM defects AS d
JOIN unfinished_tasks AS ut ON ut.id = d.task_id
ORDER BY d.title;
