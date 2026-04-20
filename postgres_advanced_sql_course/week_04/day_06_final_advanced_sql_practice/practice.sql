-- Практика: final advanced SQL practice

-- Задание 1: latest_run_dashboard
-- Верни последний test_run на каждого executor.
WITH ranked_runs AS (
    SELECT r.id,
           r.case_id,
           r.executed_by,
           r.status,
           r.duration_seconds,
           r.executed_at,
           ROW_NUMBER() OVER (
               PARTITION BY r.executed_by
               ORDER BY r.executed_at DESC, r.id DESC
           ) AS rn
    FROM test_runs AS r
)
SELECT u.name AS executor_name,
       tc.title AS case_title,
       r.id AS latest_run_id,
       r.status,
       r.duration_seconds,
       r.executed_at
FROM ranked_runs AS r
JOIN users AS u ON u.id = r.executed_by
JOIN test_cases AS tc ON tc.id = r.case_id
WHERE r.rn = 1
ORDER BY u.name;

-- Задание 2: project_points_and_rank
-- Суммируй estimate_points и отранжируй проекты.
WITH project_points AS (
    SELECT p.id,
           p.name,
           COALESCE(SUM(t.estimate_points), 0) AS total_points
    FROM projects AS p
    LEFT JOIN tasks AS t ON t.project_id = p.id
    GROUP BY p.id, p.name
)
SELECT name,
       total_points,
       DENSE_RANK() OVER (ORDER BY total_points DESC, name) AS points_rank
FROM project_points
ORDER BY points_rank, name;

-- Задание 3: daily_runs_with_zero_days
-- Построй календарь test_runs, включая пустые дни.
WITH RECURSIVE calendar AS (
    SELECT DATE '2026-04-09' AS day
    UNION ALL
    SELECT day + 1
    FROM calendar
    WHERE day < DATE '2026-04-12'
),
daily_runs AS (
    SELECT executed_at::date AS run_day,
           COUNT(*) AS runs_count
    FROM test_runs
    GROUP BY executed_at::date
)
SELECT c.day,
       COALESCE(dr.runs_count, 0) AS runs_count
FROM calendar AS c
LEFT JOIN daily_runs AS dr ON dr.run_day = c.day
ORDER BY c.day;

-- Задание 4: defect_quality_snapshot
-- Собери snapshot качества по проектам.
WITH defect_snapshot AS (
    SELECT p.id,
           p.name,
           COUNT(d.id) AS total_defects,
           COUNT(d.id) FILTER (WHERE d.status IN ('open', 'in_progress')) AS active_defects,
           COUNT(d.id) FILTER (WHERE d.severity = 'critical') AS critical_defects,
           MAX(d.reported_at) AS latest_defect_at
    FROM projects AS p
    LEFT JOIN tasks AS t ON t.project_id = p.id
    LEFT JOIN defects AS d ON d.task_id = t.id
    GROUP BY p.id, p.name
)
SELECT *
FROM defect_snapshot
ORDER BY id;

-- Задание 5: jsonb_payload_report
-- Собери compact JSONB report по проектам.
WITH project_snapshot AS (
    SELECT p.id,
           p.name,
           COUNT(t.id) AS total_tasks,
           COUNT(t.id) FILTER (WHERE t.status <> 'closed') AS unfinished_tasks,
           COUNT(d.id) FILTER (WHERE d.status IN ('open', 'in_progress')) AS active_defects
    FROM projects AS p
    LEFT JOIN tasks AS t ON t.project_id = p.id
    LEFT JOIN defects AS d ON d.task_id = t.id
    GROUP BY p.id, p.name
)
SELECT jsonb_build_object(
           'project_id', id,
           'project_name', name,
           'total_tasks', total_tasks,
           'unfinished_tasks', unfinished_tasks,
           'active_defects', active_defects
       ) AS project_payload
FROM project_snapshot
ORDER BY id;
