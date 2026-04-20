-- Практика: INSERT, UPDATE, DELETE
-- Рекомендуется выполнять каждое задание отдельно внутри BEGIN ... ROLLBACK.

-- Задание 1: insert_test_case_and_count
-- Добавь новый test_case и верни новое количество строк в test_cases.
-- expected: 5
BEGIN;
INSERT INTO test_cases (title, area, priority)
VALUES ('Temporary smoke case', 'smoke', 'low');
SELECT COUNT(*) AS test_cases_count
FROM test_cases;
ROLLBACK;

-- Задание 2: close_task_one
-- Закрой задачу id = 1 и верни её новый status.
-- expected: closed
BEGIN;
UPDATE tasks
SET status = 'closed',
    closed_at = NOW()
WHERE id = 1;
SELECT status
FROM tasks
WHERE id = 1;
ROLLBACK;

-- Задание 3: delete_fixed_defect
-- Удали defect со status = fixed и верни количество оставшихся defects.
-- expected: 2
BEGIN;
DELETE FROM defects
WHERE status = 'fixed';
SELECT COUNT(*) AS defects_left
FROM defects;
ROLLBACK;

-- Задание 4: change_priority_for_blocked_task
-- Обнови priority у задачи id = 4 до medium и верни новое значение.
-- expected: medium
BEGIN;
UPDATE tasks
SET priority = 'medium'
WHERE id = 4;
SELECT priority
FROM tasks
WHERE id = 4;
ROLLBACK;

-- Задание 5: insert_and_cleanup_user
-- Добавь временного пользователя Temp QA, затем удали его и верни count строк по имени Temp QA.
-- expected: 0
BEGIN;
INSERT INTO users (name, team, is_active)
VALUES ('Temp QA', 'qa', TRUE);
DELETE FROM users
WHERE name = 'Temp QA';
SELECT COUNT(*) AS temp_qa_count
FROM users
WHERE name = 'Temp QA';
ROLLBACK;
