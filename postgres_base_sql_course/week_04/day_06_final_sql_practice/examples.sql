-- Финальная практика: примеры составных запросов

-- Пример 1: load по проектам.
SELECT p.name AS project_name,
       COUNT(t.id) AS total_tasks,
       COUNT(t.id) FILTER (WHERE t.status <> 'closed') AS unfinished_tasks
FROM projects AS p
LEFT JOIN tasks AS t ON t.project_id = p.id
GROUP BY p.id, p.name
ORDER BY p.id;

-- Пример 2: люди, которые и владеют проектом, и репортят defects.
SELECT u.name
FROM projects AS p
JOIN users AS u ON u.id = p.owner_id
INTERSECT
SELECT u.name
FROM defects AS d
JOIN users AS u ON u.id = d.reported_by
ORDER BY name;

-- Пример 3: последний run по каждому executor.
SELECT DISTINCT ON (executed_by)
       executed_by,
       id AS latest_run_id,
       status,
       executed_at
FROM test_runs
ORDER BY executed_by, executed_at DESC;

-- Пример 4: open/in_progress defects по severity.
SELECT severity,
       COUNT(*) AS defects_count,
       STRING_AGG(title, ', ' ORDER BY title) AS defect_titles
FROM defects
WHERE status IN ('open', 'in_progress')
GROUP BY severity
ORDER BY severity;
