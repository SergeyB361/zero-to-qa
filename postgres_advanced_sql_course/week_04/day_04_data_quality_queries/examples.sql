-- Data quality queries
SELECT id, status, closed_at
FROM tasks
WHERE status = 'closed' AND closed_at IS NULL;

SELECT title, COUNT(*) AS cnt
FROM defects
GROUP BY title
HAVING COUNT(*) > 1;

SELECT d.id, d.task_id
FROM defects AS d
LEFT JOIN tasks AS t ON t.id = d.task_id
WHERE d.task_id IS NOT NULL AND t.id IS NULL;
