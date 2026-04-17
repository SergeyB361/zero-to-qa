-- Locks и blocking
-- Session A
BEGIN;
SELECT * FROM tasks WHERE id = 1 FOR UPDATE;

-- Session B
BEGIN;
UPDATE tasks SET status = 'in_progress' WHERE id = 1;

-- Session C
SELECT pid, state, wait_event_type, wait_event, query
FROM pg_stat_activity
WHERE datname = 'zero_to_qa'
ORDER BY pid;

SELECT locktype, mode, granted, pid
FROM pg_locks
WHERE pid IN (SELECT pid FROM pg_stat_activity WHERE datname = 'zero_to_qa')
ORDER BY pid, locktype, mode;
