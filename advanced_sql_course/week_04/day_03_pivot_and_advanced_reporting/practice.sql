-- Pivot-like отчёты и advanced reporting
-- Выполни setup-часть, затем замени TODO-запросы своими решениями.

-- Setup dataset
CREATE TABLE test_runs (id INTEGER PRIMARY KEY, release_tag TEXT NOT NULL, status TEXT NOT NULL);
    INSERT INTO test_runs VALUES (1, 'build-101', 'passed'), (2, 'build-101', 'failed'), (3, 'build-101', 'failed'), (4, 'build-102', 'passed'), (5, 'build-102', 'skipped'), (6, 'build-103', 'passed');

-- Задание 1: release_status_matrix
-- release status matrix
-- expected: "['build-101:1:2:0', 'build-102:1:0:1', 'build-103:1:0:0']"
-- TODO: замени заглушку реальным SQL-запросом
SELECT 'TODO: release_status_matrix' AS todo;
