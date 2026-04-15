-- Практика на JOIN и агрегации

-- Пример 1: число runs по каждому title test case.
SELECT tc.title,
       COUNT(*) AS total_runs
FROM test_runs AS tr
INNER JOIN test_cases AS tc ON tc.id = tr.case_id
GROUP BY tc.title
ORDER BY tc.title;

-- Пример 2: средняя длительность по исполнителю.
SELECT u.name,
       AVG(tr.duration_seconds) AS avg_duration
FROM test_runs AS tr
INNER JOIN users AS u ON u.id = tr.executed_by
GROUP BY u.name
ORDER BY u.name;

-- Пример 3: сколько задач у каждого проекта.
SELECT p.name,
       COUNT(t.id) AS total_tasks
FROM projects AS p
LEFT JOIN tasks AS t ON t.project_id = p.id
GROUP BY p.name
ORDER BY p.name;
