-- Recursive CTE
-- Выполни скрипт целиком в SQLite или другой совместимой среде.

-- Setup dataset
CREATE TABLE categories (id INTEGER PRIMARY KEY, name TEXT NOT NULL, parent_id INTEGER);
    INSERT INTO categories VALUES (1, 'root', NULL), (2, 'api', 1), (3, 'payments', 2), (4, 'reports', 2), (5, 'ui', 1);

-- Пример 1
WITH RECURSIVE tree AS (
            SELECT id, name, parent_id, 0 AS depth FROM categories WHERE id = 1
            UNION ALL
            SELECT c.id, c.name, c.parent_id, tree.depth + 1
            FROM categories AS c
            INNER JOIN tree ON c.parent_id = tree.id
        )
        SELECT name, depth FROM tree ORDER BY depth, id;
