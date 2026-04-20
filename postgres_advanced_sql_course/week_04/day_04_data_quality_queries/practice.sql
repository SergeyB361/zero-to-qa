-- Практика: data quality queries

-- Задание 1: closed_tasks_without_timestamp
-- Найди закрытые задачи без closed_at.
SELECT id, status, closed_at
FROM tasks
WHERE status = 'closed'
  AND closed_at IS NULL;

-- Задание 2: duplicate_defect_titles
-- Найди дубли названий defects.
SELECT title,
       COUNT(*) AS duplicate_count
FROM defects
GROUP BY title
HAVING COUNT(*) > 1
ORDER BY title;

-- Задание 3: orphan_defects_check
-- Проверь defects с несуществующим task_id.
SELECT d.id,
       d.task_id
FROM defects AS d
LEFT JOIN tasks AS t ON t.id = d.task_id
WHERE d.task_id IS NOT NULL
  AND t.id IS NULL
ORDER BY d.id;

-- Задание 4: suspicious_duration_runs
-- Найди test_runs с подозрительной длительностью.
SELECT id,
       status,
       duration_seconds,
       executed_at
FROM test_runs
WHERE duration_seconds <= 0
   OR duration_seconds > 300
ORDER BY executed_at;

-- Задание 5: blocked_tasks_with_closed_at
-- Найди blocked-задачи, у которых почему-то заполнен closed_at.
SELECT id,
       status,
       closed_at
FROM tasks
WHERE status = 'blocked'
  AND closed_at IS NOT NULL;
