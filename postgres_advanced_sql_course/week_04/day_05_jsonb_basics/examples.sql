-- JSONB basics
SELECT jsonb_build_object(
    'task_id', id,
    'status', status,
    'priority', priority
) AS task_payload
FROM tasks
ORDER BY id;

WITH payloads AS (
    SELECT id,
           jsonb_build_object('severity', severity, 'status', status) AS payload
    FROM defects
)
SELECT id,
       payload -> 'severity' AS severity_json,
       payload ->> 'status' AS status_text
FROM payloads
ORDER BY id;

WITH payloads AS (
    SELECT id,
           jsonb_build_object('team', team, 'active', is_active) AS payload
    FROM users
)
SELECT id, payload
FROM payloads
WHERE payload ->> 'team' = 'web';
