-- Практика: INSERT, UPDATE, DELETE
-- Рекомендуется выполнять каждое задание отдельно внутри BEGIN ... ROLLBACK.

-- Задание 1: insert_test_case_and_count
-- Добавь новый test_case и верни новое количество строк в test_cases.
-- expected: 5
SELECT 'TODO: insert_test_case_and_count' AS todo;

-- Задание 2: close_task_one
-- Закрой задачу id = 1 и верни её новый status.
-- expected: closed
SELECT 'TODO: close_task_one' AS todo;

-- Задание 3: delete_fixed_defect
-- Удали defect со status = fixed и верни количество оставшихся defects.
-- expected: 2
SELECT 'TODO: delete_fixed_defect' AS todo;

-- Задание 4: change_priority_for_blocked_task
-- Обнови priority у задачи id = 4 до medium и верни новое значение.
-- expected: medium
SELECT 'TODO: change_priority_for_blocked_task' AS todo;

-- Задание 5: insert_and_cleanup_user
-- Добавь временного пользователя Temp QA, затем удали его и верни count строк по имени Temp QA.
-- expected: 0
SELECT 'TODO: insert_and_cleanup_user' AS todo;
