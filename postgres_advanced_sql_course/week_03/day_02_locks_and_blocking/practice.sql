-- Практика: locks и blocking

-- Задание 1: blocking_demo_sessions
-- Запускай шаги Session A и Session B в разных psql-сессиях.
-- Session A
BEGIN;
SELECT id, status
FROM tasks
WHERE id = 1
FOR UPDATE;

-- Session B
BEGIN;
UPDATE tasks
SET status = 'in_progress'
WHERE id = 1;

-- Задание 2: inspect_pg_stat_activity
-- Посмотри, какая сессия ждёт блокировку.
SELECT pid,
       state,
       wait_event_type,
       wait_event,
       query
FROM pg_stat_activity
WHERE datname = 'zero_to_qa'
ORDER BY pid;

-- Задание 3: inspect_pg_locks
-- Посмотри granted / waiting locks по активным сессиям.
SELECT pid,
       locktype,
       relation::regclass AS relation_name,
       mode,
       granted
FROM pg_locks
WHERE pid IN (
    SELECT pid
    FROM pg_stat_activity
    WHERE datname = 'zero_to_qa'
)
ORDER BY pid, relation_name, locktype, mode;

-- Задание 4: explain_blocking_notes
-- Кратко опиши, что такое blocking.
SELECT 'Blocking means one session waits for a lock held by another session; it is a delay, not a cycle.' AS note;

-- Задание 5: safe_cleanup
-- Откати обе сессии после демонстрации.
-- Session B cleanup
ROLLBACK;

-- Session A cleanup
ROLLBACK;
