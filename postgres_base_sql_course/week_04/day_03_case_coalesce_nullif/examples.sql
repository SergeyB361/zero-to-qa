-- CASE, COALESCE, NULLIF

-- Пример 1: сгруппировать задачи по смысловым категориям.
SELECT id,
       status,
       CASE
           WHEN status = 'closed' THEN 'done'
           WHEN status = 'blocked' THEN 'risk'
           ELSE 'active'
       END AS status_bucket
FROM tasks
ORDER BY id;

-- Пример 2: показать закрыта ли задача, даже если closed_at = NULL.
SELECT id,
       COALESCE(closed_at::text, 'not closed yet') AS closed_at_text
FROM tasks
ORDER BY id;

-- Пример 3: скрыть priority = high, превратив её в NULL.
SELECT id,
       priority,
       NULLIF(priority, 'high') AS priority_without_high
FROM tasks
ORDER BY id;

-- Пример 4: вывести task_id для дефекта или текстовую метку, если task_id пустой.
SELECT id,
       title,
       COALESCE(task_id::text, 'no linked task') AS linked_task
FROM defects
ORDER BY id;
