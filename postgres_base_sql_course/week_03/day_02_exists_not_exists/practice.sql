-- Практика: EXISTS / NOT EXISTS

-- Задание 1: users_with_projects
-- Верни имена пользователей, у которых есть хотя бы один проект.
-- expected: Anna, Boris, Nina
SELECT 'TODO: users_with_projects' AS todo;

-- Задание 2: projects_without_defects
-- Верни названия проектов, где на связанных задачах нет ни одного defect.
-- expected: Mobile App
SELECT 'TODO: projects_without_defects' AS todo;

-- Задание 3: cases_without_failed_runs
-- Верни title test_cases, у которых нет ни одного failed run.
-- expected: Login works, Refresh token, Profile update
SELECT 'TODO: cases_without_failed_runs' AS todo;

-- Задание 4: tasks_with_defects
-- Верни id задач, у которых есть хотя бы один defect.
-- expected: 1, 3
SELECT 'TODO: tasks_with_defects' AS todo;

-- Задание 5: users_without_reported_defects
-- Верни имена пользователей, которые не reported ни одного defect.
-- expected: Nina, Oleg
SELECT 'TODO: users_without_reported_defects' AS todo;
