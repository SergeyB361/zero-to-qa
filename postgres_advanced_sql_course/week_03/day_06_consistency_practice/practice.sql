-- Практика: consistency

-- Задание 1: blocking_vs_deadlock_notes
-- Кратко различи blocking и deadlock.
SELECT 'Blocking is a wait on somebody else''s lock; deadlock is a cycle of waits that forces Postgres to abort one transaction.' AS note;

-- Задание 2: consistency_layers
-- Зафиксируй основные слои consistency.
SELECT 'Consistency lives in schema constraints, transaction isolation, deterministic lock ordering, and application-level retries or timeouts.' AS note;

-- Задание 3: safe_update_order_rule
-- Сформулируй правило безопасного обновления общих строк.
SELECT 'Safe rule: when multiple sessions touch the same entity set, they must lock and update rows in the same stable key order.' AS note;

-- Задание 4: inspect_integrity_on_real_table
-- Посмотри реальные constraints на defects.
SELECT con.conname AS constraint_name,
       pg_get_constraintdef(con.oid) AS definition
FROM pg_constraint AS con
JOIN pg_class AS rel ON rel.oid = con.conrelid
WHERE rel.relname = 'defects'
ORDER BY con.conname;

-- Задание 5: session_demo_outline
-- Составь короткий outline демонстрации consistency-инцидента.
WITH demo_steps AS (
    SELECT *
    FROM (
        VALUES
            ('Session A', 1, 'BEGIN; SELECT * FROM tasks WHERE id = 1 FOR UPDATE;'),
            ('Session B', 2, 'BEGIN; UPDATE tasks SET status = ''blocked'' WHERE id = 1;'),
            ('Session C', 3, 'SELECT pid, wait_event_type, query FROM pg_stat_activity WHERE datname = ''zero_to_qa'';'),
            ('Session A', 4, 'ROLLBACK;'),
            ('Session B', 5, 'ROLLBACK;')
    ) AS s(session_name, step_no, instruction)
)
SELECT session_name,
       step_no,
       instruction
FROM demo_steps
ORDER BY step_no, session_name;
