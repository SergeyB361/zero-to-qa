-- Практика: SQL anti-patterns

-- Задание 1: replace_select_star
-- Покажи rewrite запроса test_runs: вместо SELECT * оставь только нужные колонки.
-- expected: два коротких варианта, где второй уже без *
SELECT *
FROM test_runs
WHERE status = 'failed';

SELECT id, case_id, executed_by, executed_at
FROM test_runs
WHERE status = 'failed';

-- Задание 2: rewrite_date_function_filter
-- Перепиши DATE(executed_at) = ... в диапазон времени.
-- expected: filter через >= и <
SELECT id
FROM test_runs
WHERE executed_at::date = DATE '2026-04-10';

SELECT id
FROM test_runs
WHERE executed_at >= TIMESTAMPTZ '2026-04-10 00:00:00+03'
  AND executed_at < TIMESTAMPTZ '2026-04-11 00:00:00+03';

-- Задание 3: replace_distinct_with_exists
-- Перепиши DISTINCT-паттерн для проектов с задачами через EXISTS.
-- expected: EXISTS вместо DISTINCT как костыля
SELECT DISTINCT p.name
FROM projects AS p
JOIN tasks AS t ON t.project_id = p.id;

SELECT p.name
FROM projects AS p
WHERE EXISTS (
    SELECT 1
    FROM tasks AS t
    WHERE t.project_id = p.id
);

-- Задание 4: find_two_anti_patterns
-- Найди и запиши 2 анти-паттерна, которые особенно опасны для отчётов.
-- expected: краткие SQL-комментарии
-- anti-pattern 1: SELECT * в отчётах тащит лишние колонки и ломает стабильность артефактов.
-- anti-pattern 2: оборачивание indexed timestamp в функцию в WHERE мешает planner использовать индекс.
SELECT 'anti-pattern notes completed' AS note;

-- Задание 5: explain_anti_pattern_vs_rewrite
-- Для одного anti-pattern добавь EXPLAIN до и после rewrite.
-- expected: два EXPLAIN
EXPLAIN
SELECT id
FROM test_runs
WHERE executed_at::date = DATE '2026-04-10';

EXPLAIN
SELECT id
FROM test_runs
WHERE executed_at >= TIMESTAMPTZ '2026-04-10 00:00:00+03'
  AND executed_at < TIMESTAMPTZ '2026-04-11 00:00:00+03';
