-- Практика: транзакции

-- Задание 1: close_and_rollback_task
-- Напиши транзакцию, которая меняет task id = 1 на closed,
-- затем делает проверочный SELECT и завершает всё через ROLLBACK.
-- expected: после отката финальный status снова open
BEGIN;
UPDATE tasks
SET status = 'closed',
    closed_at = NOW()
WHERE id = 1;
SELECT status AS status_inside_tx
FROM tasks
WHERE id = 1;
ROLLBACK;
SELECT status AS status_after_rollback
FROM tasks
WHERE id = 1;

-- Задание 2: temp_insert_and_commit
-- Создай TEMP TABLE, вставь в неё 2 строки внутри транзакции и подтверди COMMIT.
-- expected: итоговый COUNT(*) = 2
DROP TABLE IF EXISTS tx_demo_cases;
BEGIN;
CREATE TEMP TABLE tx_demo_cases (
    id INTEGER,
    title TEXT
);
INSERT INTO tx_demo_cases (id, title)
VALUES (1, 'smoke'),
       (2, 'regression');
COMMIT;
SELECT COUNT(*) AS tx_demo_cases_count
FROM tx_demo_cases;

-- Задание 3: two_updates_one_rollback
-- На TEMP TABLE balances выполни 2 UPDATE в одной транзакции и затем ROLLBACK.
-- expected: значение возвращается к исходному
DROP TABLE IF EXISTS balances;
CREATE TEMP TABLE balances (
    id INTEGER PRIMARY KEY,
    amount INTEGER NOT NULL
);
INSERT INTO balances (id, amount)
VALUES (1, 100),
       (2, 50);
BEGIN;
UPDATE balances SET amount = amount - 10 WHERE id = 1;
UPDATE balances SET amount = amount + 10 WHERE id = 2;
SELECT id, amount
FROM balances
ORDER BY id;
ROLLBACK;
SELECT id, amount
FROM balances
ORDER BY id;

-- Задание 4: inspect_before_commit
-- Напиши сценарий: SELECT текущего статуса task id = 3,
-- затем UPDATE внутри транзакции, затем SELECT после изменения,
-- затем ROLLBACK.
-- expected: внутри транзакции status изменился, после ROLLBACK снова in_progress
BEGIN;
SELECT status AS before_update
FROM tasks
WHERE id = 3;
UPDATE tasks
SET status = 'blocked'
WHERE id = 3;
SELECT status AS after_update_inside_tx
FROM tasks
WHERE id = 3;
ROLLBACK;
SELECT status AS after_rollback
FROM tasks
WHERE id = 3;

-- Задание 5: commit_temp_update
-- Создай TEMP TABLE tx_flags, обнови одну строку внутри транзакции и подтверди COMMIT.
-- expected: финальный flag = false
DROP TABLE IF EXISTS tx_flags;
CREATE TEMP TABLE tx_flags (
    id INTEGER PRIMARY KEY,
    flag BOOLEAN NOT NULL
);
INSERT INTO tx_flags (id, flag)
VALUES (1, TRUE);
BEGIN;
UPDATE tx_flags
SET flag = FALSE
WHERE id = 1;
COMMIT;
SELECT id, flag
FROM tx_flags;
