-- Capstone: SQL investigation pack
-- Собери набор investigation-запросов по dataset zero_to_qa.

-- latest_activity_pack
DROP VIEW IF EXISTS project_activity_pack_view;
CREATE VIEW project_activity_pack_view AS
WITH latest_defect AS (
    SELECT t.project_id,
           d.id AS defect_id,
           d.title AS defect_title,
           d.status AS defect_status,
           d.reported_at,
           ROW_NUMBER() OVER (
               PARTITION BY t.project_id
               ORDER BY d.reported_at DESC, d.id DESC
           ) AS rn
    FROM defects AS d
    JOIN tasks AS t ON t.id = d.task_id
),
project_task_snapshot AS (
    SELECT p.id,
           p.name,
           COUNT(t.id) AS total_tasks,
           COUNT(t.id) FILTER (WHERE t.status <> 'closed') AS unfinished_tasks
    FROM projects AS p
    LEFT JOIN tasks AS t ON t.project_id = p.id
    GROUP BY p.id, p.name
)
SELECT pts.id,
       pts.name,
       pts.total_tasks,
       pts.unfinished_tasks,
       ld.defect_id AS latest_defect_id,
       ld.defect_title AS latest_defect_title,
       ld.defect_status AS latest_defect_status,
       ld.reported_at AS latest_defect_at
FROM project_task_snapshot AS pts
LEFT JOIN latest_defect AS ld
    ON ld.project_id = pts.id
   AND ld.rn = 1;

SELECT *
FROM project_activity_pack_view
ORDER BY id;

-- quality_pack
WITH defect_quality AS (
    SELECT t.project_id,
           COUNT(d.id) AS total_defects,
           COUNT(d.id) FILTER (WHERE d.status IN ('open', 'in_progress')) AS active_defects,
           COUNT(d.id) FILTER (WHERE d.severity = 'critical') AS critical_defects
    FROM tasks AS t
    LEFT JOIN defects AS d ON d.task_id = t.id
    GROUP BY t.project_id
)
SELECT pav.id,
       pav.name,
       pav.total_tasks,
       pav.unfinished_tasks,
       COALESCE(dq.total_defects, 0) AS total_defects,
       COALESCE(dq.active_defects, 0) AS active_defects,
       COALESCE(dq.critical_defects, 0) AS critical_defects,
       pav.latest_defect_title,
       pav.latest_defect_status,
       pav.latest_defect_at
FROM project_activity_pack_view AS pav
LEFT JOIN defect_quality AS dq ON dq.project_id = pav.id
ORDER BY pav.id;

-- time_series_pack
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
),
daily_defects AS (
    SELECT reported_at::date AS defect_day,
           COUNT(*) AS defects_count
    FROM defects
    GROUP BY reported_at::date
)
SELECT c.day,
       COALESCE(dr.runs_count, 0) AS runs_count,
       COALESCE(dd.defects_count, 0) AS defects_count,
       SUM(COALESCE(dr.runs_count, 0)) OVER (ORDER BY c.day) AS cumulative_runs
FROM calendar AS c
LEFT JOIN daily_runs AS dr ON dr.run_day = c.day
LEFT JOIN daily_defects AS dd ON dd.defect_day = c.day
ORDER BY c.day;

-- ranking_pack
WITH executor_stats AS (
    SELECT u.id,
           u.name,
           COUNT(r.id) AS total_runs,
           COUNT(r.id) FILTER (WHERE r.status = 'failed') AS failed_runs,
           COUNT(r.id) FILTER (WHERE r.status = 'blocked') AS blocked_runs,
           ROUND(COALESCE(AVG(r.duration_seconds), 0), 2) AS avg_duration
    FROM users AS u
    LEFT JOIN test_runs AS r ON r.executed_by = u.id
    GROUP BY u.id, u.name
)
SELECT name,
       total_runs,
       failed_runs,
       blocked_runs,
       avg_duration,
       DENSE_RANK() OVER (
           ORDER BY failed_runs DESC, blocked_runs DESC, avg_duration DESC, name
       ) AS investigation_rank
FROM executor_stats
ORDER BY investigation_rank, name;

-- jsonb_pack
SELECT jsonb_build_object(
           'project_id', pav.id,
           'project_name', pav.name,
           'totals', jsonb_build_object(
               'total_tasks', pav.total_tasks,
               'unfinished_tasks', pav.unfinished_tasks
           ),
           'latest_defect', CASE
               WHEN pav.latest_defect_id IS NULL THEN NULL
               ELSE jsonb_build_object(
                   'id', pav.latest_defect_id,
                   'title', pav.latest_defect_title,
                   'status', pav.latest_defect_status,
                   'reported_at', pav.latest_defect_at
               )
           END
       ) AS investigation_payload
FROM project_activity_pack_view AS pav
ORDER BY pav.id;

DROP VIEW IF EXISTS project_activity_pack_view;
