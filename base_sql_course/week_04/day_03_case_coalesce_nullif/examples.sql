-- CASE, COALESCE, NULLIF
-- Выполни скрипт целиком в SQLite или другой совместимой среде.

-- Setup dataset
CREATE TABLE tasks (id INTEGER PRIMARY KEY, title TEXT NOT NULL, priority TEXT NOT NULL, assignee TEXT, estimate_hours INTEGER NOT NULL);
    INSERT INTO tasks VALUES
        (1, 'Login works', 'high', 'Anna', 5),
        (2, 'Refund order', 'critical', NULL, 0),
        (3, 'Export report', 'low', 'Oleg', 2);

-- Пример 1
SELECT title,
               CASE WHEN priority IN ('critical', 'high') THEN 'hot' ELSE 'normal' END AS bucket,
               COALESCE(assignee, 'unassigned') AS assignee_name,
               NULLIF(estimate_hours, 0) AS normalized_estimate
        FROM tasks
        ORDER BY id;
