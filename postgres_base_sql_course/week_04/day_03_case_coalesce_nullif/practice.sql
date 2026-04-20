-- Практика: CASE, COALESCE, NULLIF

-- Задание 1: task_status_bucket
-- Верни id, status и bucket:
-- closed -> done, blocked -> risk, остальные -> active.
-- expected: done = 1, risk = 1, active = 2
SELECT id,
       status,
       CASE
           WHEN status = 'closed' THEN 'done'
           WHEN status = 'blocked' THEN 'risk'
           ELSE 'active'
       END AS bucket
FROM tasks
ORDER BY id;

-- Задание 2: closed_at_label
-- Верни id и COALESCE для closed_at, чтобы незакрытые задачи показывались как 'not closed yet'.
-- expected: только task id = 2 имеет реальное timestamp-значение
SELECT id,
       COALESCE(closed_at::text, 'not closed yet') AS closed_at_label
FROM tasks
ORDER BY id;

-- Задание 3: priority_without_high
-- Верни id и NULLIF(priority, 'high').
-- expected: для задач с priority = high результат NULL
SELECT id,
       NULLIF(priority, 'high') AS priority_without_high
FROM tasks
ORDER BY id;

-- Задание 4: linked_task_label
-- Верни defects с task_id::text, а при NULL покажи 'no linked task'.
-- expected: defect id = 1 показывает linked task 2, defect id = 3 показывает linked task 3
SELECT id,
       title,
       COALESCE(task_id::text, 'no linked task') AS linked_task_label
FROM defects
ORDER BY id;

-- Задание 5: run_result_label
-- Через CASE верни id и label:
-- passed -> good, failed -> investigate, blocked -> pending.
-- expected: good = 2, investigate = 1, pending = 1
SELECT id,
       CASE
           WHEN status = 'passed' THEN 'good'
           WHEN status = 'failed' THEN 'investigate'
           WHEN status = 'blocked' THEN 'pending'
       END AS run_label
FROM test_runs
ORDER BY id;
