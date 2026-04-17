-- Практика: join optimization

-- Задание 1: defects_per_project_naive
-- Напиши наивный join-запрос projects -> tasks -> defects с GROUP BY.
-- expected: обычный join + aggregate
SELECT 'TODO: defects_per_project_naive' AS todo;

-- Задание 2: defects_per_project_preaggregated
-- Перепиши задачу через CTE, где defects сначала агрегируются по task_id.
-- expected: CTE + join уже агрегированного слоя
SELECT 'TODO: defects_per_project_preaggregated' AS todo;

-- Задание 3: open_defects_filtered_before_join
-- Сначала отфильтруй open/in_progress defects, затем join к tasks/projects.
-- expected: CTE open_defects + итоговый report
SELECT 'TODO: open_defects_filtered_before_join' AS todo;

-- Задание 4: choose_join_type
-- Напиши 2 коротких комментария: где в dataset уместен INNER JOIN, а где LEFT JOIN.
-- expected: осмысленные примеры по projects/tasks/defects
SELECT 'TODO: choose_join_type' AS todo;

-- Задание 5: explain_join_rewrite
-- Для наивного и переписанного варианта добавь EXPLAIN.
-- expected: два EXPLAIN и два варианта join-логики
SELECT 'TODO: explain_join_rewrite' AS todo;
