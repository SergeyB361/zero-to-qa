-- Set operations

-- Пример 1: project owners или defect reporters.
SELECT u.name
FROM projects AS p
JOIN users AS u ON u.id = p.owner_id
UNION
SELECT u.name
FROM defects AS d
JOIN users AS u ON u.id = d.reported_by
ORDER BY name;

-- Пример 2: та же идея, но с сохранением дублей.
SELECT u.name
FROM projects AS p
JOIN users AS u ON u.id = p.owner_id
UNION ALL
SELECT u.name
FROM defects AS d
JOIN users AS u ON u.id = d.reported_by
ORDER BY name;

-- Пример 3: пользователи, которые и назначены на задачи, и владеют проектом.
SELECT u.name
FROM tasks AS t
JOIN users AS u ON u.id = t.assignee_id
INTERSECT
SELECT u.name
FROM projects AS p
JOIN users AS u ON u.id = p.owner_id
ORDER BY name;

-- Пример 4: assignees, которые не являются owner проекта.
SELECT u.name
FROM tasks AS t
JOIN users AS u ON u.id = t.assignee_id
EXCEPT
SELECT u.name
FROM projects AS p
JOIN users AS u ON u.id = p.owner_id
ORDER BY name;
