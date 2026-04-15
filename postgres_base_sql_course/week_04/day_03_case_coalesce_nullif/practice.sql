-- Практика: CASE, COALESCE, NULLIF

-- Задание 1: task_status_bucket
-- Верни id, status и bucket:
-- closed -> done, blocked -> risk, остальные -> active.
-- expected: done = 1, risk = 1, active = 2
SELECT 'TODO: task_status_bucket' AS todo;

-- Задание 2: closed_at_label
-- Верни id и COALESCE для closed_at, чтобы незакрытые задачи показывались как 'not closed yet'.
-- expected: только task id = 2 имеет реальное timestamp-значение
SELECT 'TODO: closed_at_label' AS todo;

-- Задание 3: priority_without_high
-- Верни id и NULLIF(priority, 'high').
-- expected: для задач с priority = high результат NULL
SELECT 'TODO: priority_without_high' AS todo;

-- Задание 4: linked_task_label
-- Верни defects с task_id::text, а при NULL покажи 'no linked task'.
-- expected: defect id = 1 показывает linked task 2, defect id = 3 показывает linked task 3
SELECT 'TODO: linked_task_label' AS todo;

-- Задание 5: run_result_label
-- Через CASE верни id и label:
-- passed -> good, failed -> investigate, blocked -> pending.
-- expected: good = 2, investigate = 1, pending = 1
SELECT 'TODO: run_result_label' AS todo;
