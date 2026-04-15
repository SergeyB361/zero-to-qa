-- Практика: JOIN и агрегации

-- Задание 1: runs_per_case
-- Верни title test case и COUNT(*) запусков.
-- expected: Login works = 1, Create order = 1, Refresh token = 1, Profile update = 1
SELECT 'TODO: runs_per_case' AS todo;

-- Задание 2: avg_duration_per_executor
-- Верни имя пользователя и AVG(duration_seconds) его запусков.
-- expected: Boris имеет среднее > 40
SELECT 'TODO: avg_duration_per_executor' AS todo;

-- Задание 3: tasks_per_project
-- Верни project name и COUNT(task id).
-- expected: Public API = 1
SELECT 'TODO: tasks_per_project' AS todo;

-- Задание 4: open_defects_per_reporter
-- Верни reporter name и COUNT(open/in_progress defects).
-- expected: Anna = 1, Boris = 1
SELECT 'TODO: open_defects_per_reporter' AS todo;

-- Задание 5: runs_per_status_with_titles
-- Верни title test case, status и COUNT(*) по комбинациям.
-- expected: Create order / failed = 1
SELECT 'TODO: runs_per_status_with_titles' AS todo;
