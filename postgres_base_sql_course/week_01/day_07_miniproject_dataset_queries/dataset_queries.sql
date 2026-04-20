-- Мини-проект: dataset queries
-- Используй базу zero_to_qa из postgres_lab.

-- list_active_users
-- expected: Anna, Boris, Oleg
SELECT id,
       name,
       team
FROM users
WHERE is_active = TRUE
ORDER BY name;

-- high_priority_cases
-- expected: Login works, Create order, Refresh token
SELECT id,
       title,
       priority
FROM test_cases
WHERE priority IN ('high', 'critical')
ORDER BY priority DESC, id;

-- unfinished_task_ids
-- expected: 1, 3, 4
SELECT id,
       status
FROM tasks
WHERE status <> 'closed'
ORDER BY id;

-- failed_run_ids
-- expected: 2
SELECT id,
       case_id,
       executed_by
FROM test_runs
WHERE status = 'failed';

-- open_defects
-- expected: Login 500, Refresh loop
SELECT id,
       title,
       severity,
       status
FROM defects
WHERE status IN ('open', 'in_progress')
ORDER BY id;
