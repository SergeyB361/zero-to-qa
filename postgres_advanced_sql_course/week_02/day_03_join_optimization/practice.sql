-- Практика: join optimization

-- Задание 1: defects_per_project_naive
-- Напиши наивный join-запрос projects -> tasks -> defects с GROUP BY.
-- expected: обычный join + aggregate
SELECT p.name,
       COUNT(d.id) AS defects_count
FROM projects AS p
LEFT JOIN tasks AS t ON t.project_id = p.id
LEFT JOIN defects AS d ON d.task_id = t.id
GROUP BY p.id, p.name
ORDER BY p.id;

-- Задание 2: defects_per_project_preaggregated
-- Перепиши задачу через CTE, где defects сначала агрегируются по task_id.
-- expected: CTE + join уже агрегированного слоя
WITH defect_counts AS (
    SELECT task_id,
           COUNT(*) AS defects_count
    FROM defects
    GROUP BY task_id
)
SELECT p.name,
       COALESCE(SUM(dc.defects_count), 0) AS defects_count
FROM projects AS p
LEFT JOIN tasks AS t ON t.project_id = p.id
LEFT JOIN defect_counts AS dc ON dc.task_id = t.id
GROUP BY p.id, p.name
ORDER BY p.id;

-- Задание 3: open_defects_filtered_before_join
-- Сначала отфильтруй open/in_progress defects, затем join к tasks/projects.
-- expected: CTE open_defects + итоговый report
WITH open_defects AS (
    SELECT task_id,
           COUNT(*) AS active_defects
    FROM defects
    WHERE status IN ('open', 'in_progress')
    GROUP BY task_id
)
SELECT p.name,
       COALESCE(SUM(od.active_defects), 0) AS active_defects
FROM projects AS p
LEFT JOIN tasks AS t ON t.project_id = p.id
LEFT JOIN open_defects AS od ON od.task_id = t.id
GROUP BY p.id, p.name
ORDER BY p.id;

-- Задание 4: choose_join_type
-- Напиши 2 коротких комментария: где в dataset уместен INNER JOIN, а где LEFT JOIN.
-- expected: осмысленные примеры по projects/tasks/defects
-- INNER JOIN: test_runs -> test_cases, когда нужны только реально существующие запуски и их кейсы.
-- LEFT JOIN: projects -> tasks, когда проект должен остаться в отчёте даже без связанных задач.
SELECT 'join type notes completed' AS note;

-- Задание 5: explain_join_rewrite
-- Для наивного и переписанного варианта добавь EXPLAIN.
-- expected: два EXPLAIN и два варианта join-логики
EXPLAIN
SELECT p.name,
       COUNT(d.id) AS defects_count
FROM projects AS p
LEFT JOIN tasks AS t ON t.project_id = p.id
LEFT JOIN defects AS d ON d.task_id = t.id
GROUP BY p.id, p.name;

EXPLAIN
WITH defect_counts AS (
    SELECT task_id,
           COUNT(*) AS defects_count
    FROM defects
    GROUP BY task_id
)
SELECT p.name,
       COALESCE(SUM(dc.defects_count), 0) AS defects_count
FROM projects AS p
LEFT JOIN tasks AS t ON t.project_id = p.id
LEFT JOIN defect_counts AS dc ON dc.task_id = t.id
GROUP BY p.id, p.name;
