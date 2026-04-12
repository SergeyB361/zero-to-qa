-- UNION, UNION ALL, INTERSECT, EXCEPT
-- Выполни скрипт целиком в SQLite или другой совместимой среде.

-- Setup dataset
CREATE TABLE web_owners (name TEXT NOT NULL);
    CREATE TABLE api_owners (name TEXT NOT NULL);
    INSERT INTO web_owners VALUES ('Anna'), ('Oleg'), ('Nina');
    INSERT INTO api_owners VALUES ('Boris'), ('Anna'), ('Nina'), ('Nina');

-- Пример 1
UNION ->;

-- Пример 2
SELECT name FROM web_owners UNION SELECT name FROM api_owners ORDER BY name;

-- Пример 3
UNION ALL ->;

-- Пример 4
SELECT name FROM web_owners UNION ALL SELECT name FROM api_owners ORDER BY name;

-- Пример 5
INTERSECT ->;

-- Пример 6
SELECT name FROM web_owners INTERSECT SELECT name FROM api_owners ORDER BY name;

-- Пример 7
EXCEPT ->;

-- Пример 8
SELECT name FROM web_owners EXCEPT SELECT name FROM api_owners ORDER BY name;
