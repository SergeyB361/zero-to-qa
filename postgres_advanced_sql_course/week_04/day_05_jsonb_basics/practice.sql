-- Практика: JSONB basics

-- Задание 1: build_task_payload
-- Собери JSONB payload по задачам.
SELECT jsonb_build_object(
           'task_id', t.id,
           'project', p.name,
           'assignee', u.name,
           'status', t.status,
           'priority', t.priority,
           'estimate_points', t.estimate_points
       ) AS task_payload
FROM tasks AS t
JOIN projects AS p ON p.id = t.project_id
JOIN users AS u ON u.id = t.assignee_id
ORDER BY t.id;

-- Задание 2: extract_defect_fields_from_jsonb
-- Извлеки поля из JSONB payload по defects.
WITH defect_payloads AS (
    SELECT id,
           jsonb_build_object(
               'title', title,
               'severity', severity,
               'status', status
           ) AS payload
    FROM defects
)
SELECT id,
       payload ->> 'title' AS title,
       payload -> 'severity' AS severity_json,
       payload ->> 'status' AS status_text
FROM defect_payloads
ORDER BY id;

-- Задание 3: filter_users_by_jsonb_team
-- Отфильтруй payload по team.
WITH user_payloads AS (
    SELECT id,
           name,
           jsonb_build_object(
               'team', team,
               'active', is_active
           ) AS payload
    FROM users
)
SELECT id,
       name,
       payload
FROM user_payloads
WHERE payload ->> 'team' = 'web'
ORDER BY id;

-- Задание 4: jsonb_key_presence_comment
-- Кратко объясни проверку наличия ключа.
SELECT 'Use payload ? ''team'' to check key presence; use -> for JSONB and ->> for plain text extraction.' AS note;

-- Задание 5: compare_arrow_operators
-- Покажи разницу между -> и ->>.
WITH sample_payload AS (
    SELECT jsonb_build_object(
               'team', team,
               'active', is_active
           ) AS payload
    FROM users
    WHERE id = 1
)
SELECT payload -> 'team' AS team_json,
       payload ->> 'team' AS team_text,
       payload -> 'active' AS active_json,
       payload ->> 'active' AS active_text
FROM sample_payload;
