-- Мини-проект: optimization lab
-- Собери SQL-lab по performance-кейсам на базе zero_to_qa.

-- lookup_case
EXPLAIN
SELECT id, title, severity
FROM defects
WHERE reported_at >= TIMESTAMPTZ '2026-04-09 09:00:00+03';

-- join_case
EXPLAIN
WITH active_defects AS (
    SELECT task_id,
           COUNT(*) AS active_defects_count
    FROM defects
    WHERE status IN ('open', 'in_progress')
    GROUP BY task_id
)
SELECT p.name,
       COUNT(t.id) AS total_tasks,
       COALESCE(SUM(ad.active_defects_count), 0) AS active_defects
FROM projects AS p
LEFT JOIN tasks AS t ON t.project_id = p.id
LEFT JOIN active_defects AS ad ON ad.task_id = t.id
GROUP BY p.id, p.name;

-- time_filter_case
EXPLAIN
SELECT id
FROM test_runs
WHERE executed_at >= TIMESTAMPTZ '2026-04-10 00:00:00+03'
  AND executed_at < TIMESTAMPTZ '2026-04-11 00:00:00+03';

-- anti_pattern_case
EXPLAIN
SELECT DISTINCT p.name
FROM projects AS p
JOIN tasks AS t ON t.project_id = p.id;
