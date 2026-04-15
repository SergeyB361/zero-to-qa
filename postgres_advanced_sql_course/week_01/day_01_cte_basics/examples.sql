-- CTE basics

-- Пример 1: вынести незакрытые задачи в отдельный слой.
WITH unfinished_tasks AS (
    SELECT id, project_id, assignee_id, status, estimate_points
    FROM tasks
    WHERE status <> 'closed'
)
SELECT id, status, estimate_points
FROM unfinished_tasks
ORDER BY id;

-- Пример 2: сначала посчитать задачи по проектам, затем присоединить имя проекта.
WITH project_task_stats AS (
    SELECT project_id,
           COUNT(*) AS total_tasks,
           COUNT(*) FILTER (WHERE status <> 'closed') AS unfinished_tasks
    FROM tasks
    GROUP BY project_id
)
SELECT p.name,
       s.total_tasks,
       s.unfinished_tasks
FROM project_task_stats AS s
JOIN projects AS p ON p.id = s.project_id
ORDER BY p.id;

-- Пример 3: вынести runs по исполнителям и затем агрегировать.
WITH run_base AS (
    SELECT executed_by, duration_seconds
    FROM test_runs
)
SELECT u.name,
       COUNT(*) AS runs_count,
       AVG(r.duration_seconds) AS avg_duration
FROM run_base AS r
JOIN users AS u ON u.id = r.executed_by
GROUP BY u.id, u.name
ORDER BY u.name;
