-- Практика: SQL anti-patterns

-- Задание 1: replace_select_star
-- Покажи rewrite запроса test_runs: вместо SELECT * оставь только нужные колонки.
-- expected: два коротких варианта, где второй уже без *
SELECT 'TODO: replace_select_star' AS todo;

-- Задание 2: rewrite_date_function_filter
-- Перепиши DATE(executed_at) = ... в диапазон времени.
-- expected: filter через >= и <
SELECT 'TODO: rewrite_date_function_filter' AS todo;

-- Задание 3: replace_distinct_with_exists
-- Перепиши DISTINCT-паттерн для проектов с задачами через EXISTS.
-- expected: EXISTS вместо DISTINCT как костыля
SELECT 'TODO: replace_distinct_with_exists' AS todo;

-- Задание 4: find_two_anti_patterns
-- Найди и запиши 2 анти-паттерна, которые особенно опасны для отчётов.
-- expected: краткие SQL-комментарии
SELECT 'TODO: find_two_anti_patterns' AS todo;

-- Задание 5: explain_anti_pattern_vs_rewrite
-- Для одного anti-pattern добавь EXPLAIN до и после rewrite.
-- expected: два EXPLAIN
SELECT 'TODO: explain_anti_pattern_vs_rewrite' AS todo;
