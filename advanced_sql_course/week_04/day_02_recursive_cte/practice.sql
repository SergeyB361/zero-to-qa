-- Recursive CTE
-- Выполни setup-часть, затем замени TODO-запросы своими решениями.

-- Setup dataset
CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT NOT NULL, manager_id INTEGER);
    INSERT INTO employees VALUES (1, 'CTO', NULL), (2, 'QA Lead', 1), (3, 'Backend Lead', 1), (4, 'QA Engineer', 2), (5, 'Automation Engineer', 2);

-- Задание 1: management_chain
-- management chain
-- expected: "['QA Engineer', 'QA Lead', 'CTO']"
-- TODO: замени заглушку реальным SQL-запросом
SELECT 'TODO: management_chain' AS todo;

-- Задание 2: qa_subtree
-- qa subtree
-- expected: "['Automation Engineer', 'QA Engineer', 'QA Lead']"
-- TODO: замени заглушку реальным SQL-запросом
SELECT 'TODO: qa_subtree' AS todo;
