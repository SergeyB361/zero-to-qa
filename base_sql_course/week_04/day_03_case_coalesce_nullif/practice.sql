-- CASE, COALESCE, NULLIF
-- Выполни setup-часть, затем замени TODO-запросы своими решениями.

-- Setup dataset
CREATE TABLE defects (id INTEGER PRIMARY KEY, title TEXT NOT NULL, severity TEXT NOT NULL, owner TEXT, resolved_hours INTEGER NOT NULL);
    INSERT INTO defects VALUES
        (1, 'Login 500', 'critical', 'Boris', 4),
        (2, 'Wrong total', 'major', NULL, 0),
        (3, 'Slow export', 'minor', 'Anna', 12);

-- Задание 1: severity_labels
-- severity labels
-- expected: "['Login 500:hot', 'Wrong total:hot', 'Slow export:normal']"
-- TODO: замени заглушку реальным SQL-запросом
SELECT 'TODO: severity_labels' AS todo;

-- Задание 2: owner_or_unassigned
-- owner or unassigned
-- expected: "['Boris', 'unassigned', 'Anna']"
-- TODO: замени заглушку реальным SQL-запросом
SELECT 'TODO: owner_or_unassigned' AS todo;

-- Задание 3: normalized_resolution_hours
-- normalized resolution hours
-- expected: '[4, None, 12]'
-- TODO: замени заглушку реальным SQL-запросом
SELECT 'TODO: normalized_resolution_hours' AS todo;

-- Задание 4: resolution_speed_labels
-- Верни пары title:label, где fast для <= 4 часов, none для 0, slow для остальных.
-- expected: "['Login 500:fast', 'Wrong total:none', 'Slow export:slow']"
-- TODO: замени заглушку реальным SQL-запросом
SELECT 'TODO: resolution_speed_labels' AS todo;

-- Задание 5: safe_resolution_hours
-- Замени 0 часов на -1 через NULLIF и COALESCE.
-- expected: '[4, -1, 12]'
-- TODO: замени заглушку реальным SQL-запросом
SELECT 'TODO: safe_resolution_hours' AS todo;
