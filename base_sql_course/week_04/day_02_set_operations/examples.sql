-- UNION, UNION ALL, INTERSECT, EXCEPT
-- Выполни скрипт целиком в SQLite или другой совместимой среде.

-- Setup dataset
CREATE TABLE web_owners (name TEXT NOT NULL);
CREATE TABLE api_owners (name TEXT NOT NULL);
INSERT INTO web_owners VALUES ('Anna'), ('Oleg'), ('Nina');
INSERT INTO api_owners VALUES ('Boris'), ('Anna'), ('Nina'), ('Nina');

-- Пример 1: объединить уникальные имена
SELECT name FROM web_owners
UNION
SELECT name FROM api_owners
ORDER BY name;

-- Пример 2: объединить все имена, не удаляя повторы
SELECT name FROM web_owners
UNION ALL
SELECT name FROM api_owners
ORDER BY name;

-- Пример 3: оставить только общие имена
SELECT name FROM web_owners
INTERSECT
SELECT name FROM api_owners
ORDER BY name;

-- Пример 4: оставить имена только из первой выборки
SELECT name FROM web_owners
EXCEPT
SELECT name FROM api_owners
ORDER BY name;