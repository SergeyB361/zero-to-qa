-- UNION, UNION ALL, INTERSECT, EXCEPT
-- Выполни setup-часть, затем замени TODO-запросы своими решениями.

-- Setup dataset
CREATE TABLE release_101_failed (title TEXT NOT NULL);
    CREATE TABLE release_102_failed (title TEXT NOT NULL);
    INSERT INTO release_101_failed VALUES ('Login works'), ('Create order'), ('Refund order');
    INSERT INTO release_102_failed VALUES ('Create order'), ('Filter products'), ('Refund order'), ('Refund order');

-- Задание 1: all_failed_titles
-- all failed titles
-- expected: "['Create order', 'Filter products', 'Login works', 'Refund order']"
-- TODO: замени заглушку реальным SQL-запросом
SELECT 'TODO: all_failed_titles' AS todo;

-- Задание 2: repeated_failures
-- repeated failures
-- expected: "['Create order', 'Refund order']"
-- TODO: замени заглушку реальным SQL-запросом
SELECT 'TODO: repeated_failures' AS todo;

-- Задание 3: only_first_release_failures
-- only first release failures
-- expected: "['Login works']"
-- TODO: замени заглушку реальным SQL-запросом
SELECT 'TODO: only_first_release_failures' AS todo;
