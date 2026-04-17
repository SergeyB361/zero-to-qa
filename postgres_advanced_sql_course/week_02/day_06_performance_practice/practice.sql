-- Практика: performance

-- Задание 1: choose_index_for_lookup
-- Выбери lookup-запрос из dataset и предложи осмысленный индекс.
-- expected: CREATE INDEX + короткий комментарий зачем он нужен
SELECT 'TODO: choose_index_for_lookup' AS todo;

-- Задание 2: explain_before_after_index
-- На TEMP TABLE покажи план до и после индекса.
-- expected: два EXPLAIN и один CREATE INDEX
SELECT 'TODO: explain_before_after_index' AS todo;

-- Задание 3: rewrite_time_filter
-- Перепиши time-filter без DATE(...) в WHERE и добавь EXPLAIN.
-- expected: rewrite через диапазон и EXPLAIN
SELECT 'TODO: rewrite_time_filter' AS todo;

-- Задание 4: optimize_join_report
-- Возьми join-report по projects/tasks/defects и предложи более лёгкую форму через CTE.
-- expected: rewrite, где detail слой сокращается заранее
SELECT 'TODO: optimize_join_report' AS todo;

-- Задание 5: performance_reasoning_notes
-- Напиши 3 SQL-комментария: когда нужен индекс, когда нужен rewrite, когда нужен EXPLAIN ANALYZE.
-- expected: 3 коротких осмысленных комментария
SELECT 'TODO: performance_reasoning_notes' AS todo;
