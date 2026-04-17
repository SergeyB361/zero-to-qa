-- Join optimization

-- Пример 1: наивный подход - join raw tables и потом aggregate.
EXPLAIN
SELECT p.name,
       COUNT(d.id) AS defects_count
FROM projects AS p
JOIN tasks AS t ON t.project_id = p.id
LEFT JOIN defects AS d ON d.task_id = t.id
GROUP BY p.id, p.name;

-- Пример 2: сначала считаем defects по tasks, потом join к проектам.
EXPLAIN
WITH task_defects AS (
    SELECT task_id,
           COUNT(*) AS defects_count
    FROM defects
    GROUP BY task_id
)
SELECT p.name,
       COALESCE(SUM(td.defects_count), 0) AS defects_count
FROM projects AS p
JOIN tasks AS t ON t.project_id = p.id
LEFT JOIN task_defects AS td ON td.task_id = t.id
GROUP BY p.id, p.name;

-- Пример 3: фильтруем открытые defects до join.
EXPLAIN
WITH open_defects AS (
    SELECT task_id
    FROM defects
    WHERE status IN ('open', 'in_progress')
)
SELECT p.name,
       COUNT(od.task_id) AS open_defects_count
FROM projects AS p
JOIN tasks AS t ON t.project_id = p.id
LEFT JOIN open_defects AS od ON od.task_id = t.id
GROUP BY p.id, p.name;
