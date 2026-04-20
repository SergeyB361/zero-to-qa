-- Мини-проект: transaction scenarios
-- Собери демонстрационные сценарии по isolation, blocking и deadlocks.

-- isolation_case
-- Session A
BEGIN;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
SELECT id, status
FROM tasks
WHERE id = 1;

-- Session B
BEGIN;
UPDATE tasks
SET status = 'in_progress'
WHERE id = 1;
COMMIT;

-- Session A
SELECT id, status
FROM tasks
WHERE id = 1;
ROLLBACK;

-- isolation_case cleanup
UPDATE tasks
SET status = 'open'
WHERE id = 1;

-- blocking_case
-- Session A
BEGIN;
SELECT id, status
FROM tasks
WHERE id = 3
FOR UPDATE;

-- Session B
BEGIN;
UPDATE tasks
SET status = 'in_progress'
WHERE id = 3;

-- blocking_case cleanup
-- Session B cleanup
ROLLBACK;

-- Session A cleanup
ROLLBACK;

-- deadlock_case
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

-- deadlock_case cleanup
ROLLBACK;
ROLLBACK;

-- inspection_queries
SELECT pid,
       state,
       wait_event_type,
       wait_event,
       query
FROM pg_stat_activity
WHERE datname = 'zero_to_qa'
ORDER BY pid;

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
