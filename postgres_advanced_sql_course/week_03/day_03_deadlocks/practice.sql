-- Практика: deadlocks

-- Задание 1: two_session_deadlock_demo
-- Запускай Session A и Session B в разных окнах, чтобы получить deadlock.
-- Session A
BEGIN;
UPDATE tasks
SET estimate_points = estimate_points + 1
WHERE id = 1;
UPDATE tasks
SET estimate_points = estimate_points + 1
WHERE id = 2;

-- Session B
BEGIN;
UPDATE tasks
SET estimate_points = estimate_points + 1
WHERE id = 2;
UPDATE tasks
SET estimate_points = estimate_points + 1
WHERE id = 1;

-- Задание 2: explain_cycle
-- Объясни цикл ожидания.
SELECT 'Deadlock appears when session A waits on a row locked by session B while session B simultaneously waits on a row locked by session A.' AS note;

-- Задание 3: safe_ordering_strategy
-- Зафиксируй безопасную стратегию.
SELECT 'Safe strategy: all sessions must lock and update shared rows in the same deterministic order, for example by ascending id.' AS note;

-- Задание 4: identify_deadlock_vs_blocking
-- Кратко различи deadlock и blocking.
SELECT 'Blocking is a one-way wait; deadlock is a wait cycle, so Postgres aborts one transaction with deadlock detected.' AS note;

-- Задание 5: rollback_cleanup
-- После демонстрации откати оставшиеся транзакции.
ROLLBACK;
ROLLBACK;
