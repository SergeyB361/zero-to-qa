-- Deadlocks
-- Session A
BEGIN;
UPDATE tasks SET estimate_points = estimate_points + 1 WHERE id = 1;
UPDATE tasks SET estimate_points = estimate_points + 1 WHERE id = 2;

-- Session B
BEGIN;
UPDATE tasks SET estimate_points = estimate_points + 1 WHERE id = 2;
UPDATE tasks SET estimate_points = estimate_points + 1 WHERE id = 1;

-- Один из сеансов получит deadlock detected.
ROLLBACK;
