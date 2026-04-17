-- Views и materialized views
DROP VIEW IF EXISTS project_task_overview;
CREATE VIEW project_task_overview AS
SELECT p.id,
       p.name,
       COUNT(t.id) AS total_tasks,
       COUNT(t.id) FILTER (WHERE t.status <> 'closed') AS unfinished_tasks
FROM projects AS p
LEFT JOIN tasks AS t ON t.project_id = p.id
GROUP BY p.id, p.name;

SELECT * FROM project_task_overview ORDER BY id;

DROP MATERIALIZED VIEW IF EXISTS defect_severity_snapshot;
CREATE MATERIALIZED VIEW defect_severity_snapshot AS
SELECT severity,
       COUNT(*) AS defects_count
FROM defects
GROUP BY severity;

SELECT * FROM defect_severity_snapshot ORDER BY severity;
REFRESH MATERIALIZED VIEW defect_severity_snapshot;
