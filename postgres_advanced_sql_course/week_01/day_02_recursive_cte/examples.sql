-- Recursive CTE

-- Пример 1: простая последовательность чисел.
WITH RECURSIVE numbers AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n + 1
    FROM numbers
    WHERE n < 5
)
SELECT n
FROM numbers
ORDER BY n;

-- Пример 2: календарь из трёх дней.
WITH RECURSIVE calendar AS (
    SELECT DATE '2026-04-09' AS day
    UNION ALL
    SELECT day + 1
    FROM calendar
    WHERE day < DATE '2026-04-11'
)
SELECT day
FROM calendar
ORDER BY day;

-- Пример 3: календарь + количество runs по дням.
WITH RECURSIVE calendar AS (
    SELECT DATE '2026-04-09' AS day
    UNION ALL
    SELECT day + 1
    FROM calendar
    WHERE day < DATE '2026-04-11'
)
SELECT c.day,
       COUNT(tr.id) AS runs_count
FROM calendar AS c
LEFT JOIN test_runs AS tr ON tr.executed_at::date = c.day
GROUP BY c.day
ORDER BY c.day;
