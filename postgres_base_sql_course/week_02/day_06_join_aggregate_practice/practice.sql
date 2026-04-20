-- Практика: JOIN и агрегации

-- Задание 1: runs_per_case
-- Верни title test case и COUNT(*) запусков.
-- expected: Login works = 1, Create order = 1, Refresh token = 1, Profile update = 1
SELECT c.title,
       COUNT(r.id) AS runs_count
FROM test_cases AS c
JOIN test_runs AS r ON r.case_id = c.id
GROUP BY c.id, c.title
ORDER BY c.id;

-- Задание 2: avg_duration_per_executor
-- Верни имя пользователя и AVG(duration_seconds) его запусков.
-- expected: Boris имеет среднее > 40
SELECT u.name,
       ROUND(AVG(r.duration_seconds), 2) AS avg_duration
FROM test_runs AS r
JOIN users AS u ON u.id = r.executed_by
GROUP BY u.id, u.name
ORDER BY u.name;

-- Задание 3: tasks_per_project
-- Верни project name и COUNT(task id).
-- expected: Public API = 1
SELECT p.name AS project_name,
       COUNT(t.id) AS tasks_count
FROM projects AS p
LEFT JOIN tasks AS t ON t.project_id = p.id
GROUP BY p.id, p.name
ORDER BY p.id;

-- Задание 4: open_defects_per_reporter
-- Верни reporter name и COUNT(open/in_progress defects).
-- expected: Anna = 1, Boris = 1
SELECT u.name AS reporter_name,
       COUNT(d.id) AS active_defects_count
FROM defects AS d
JOIN users AS u ON u.id = d.reported_by
WHERE d.status IN ('open', 'in_progress')
GROUP BY u.id, u.name
ORDER BY u.name;

-- Задание 5: runs_per_status_with_titles
-- Верни title test case, status и COUNT(*) по комбинациям.
-- expected: Create order / failed = 1
SELECT c.title,
       r.status,
       COUNT(*) AS runs_count
FROM test_runs AS r
JOIN test_cases AS c ON c.id = r.case_id
GROUP BY c.id, c.title, r.status
ORDER BY c.id, r.status;
