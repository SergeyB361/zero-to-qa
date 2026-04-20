-- Практика: recursive CTE

-- Задание 1: numbers_1_to_5
-- Через recursive CTE верни числа от 1 до 5.
-- expected: 1, 2, 3, 4, 5
WITH RECURSIVE numbers AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n + 1
    FROM numbers
    WHERE n < 5
)
SELECT n
FROM numbers;

-- Задание 2: countdown_4_to_1
-- Через recursive CTE верни числа 4, 3, 2, 1.
-- expected: 4, 3, 2, 1
WITH RECURSIVE countdown AS (
    SELECT 4 AS n
    UNION ALL
    SELECT n - 1
    FROM countdown
    WHERE n > 1
)
SELECT n
FROM countdown;

-- Задание 3: calendar_2026_04_09_to_2026_04_11
-- Через recursive CTE построй календарь с 2026-04-09 по 2026-04-11.
-- expected: 2026-04-09, 2026-04-10, 2026-04-11
WITH RECURSIVE calendar AS (
    SELECT DATE '2026-04-09' AS day
    UNION ALL
    SELECT day + 1
    FROM calendar
    WHERE day < DATE '2026-04-11'
)
SELECT day
FROM calendar;

-- Задание 4: run_counts_by_recursive_calendar
-- Построй календарь на 2026-04-09 .. 2026-04-11 и посчитай runs_count по дням.
-- expected:
-- 2026-04-09 -> 0
-- 2026-04-10 -> 4
-- 2026-04-11 -> 0
WITH RECURSIVE calendar AS (
    SELECT DATE '2026-04-09' AS day
    UNION ALL
    SELECT day + 1
    FROM calendar
    WHERE day < DATE '2026-04-11'
)
SELECT c.day,
       COUNT(r.id) AS runs_count
FROM calendar AS c
LEFT JOIN test_runs AS r
    ON (r.executed_at AT TIME ZONE 'Europe/Moscow')::date = c.day
GROUP BY c.day
ORDER BY c.day;

-- Задание 5: recursive_sum_to_4
-- Через recursive CTE построй числа 1..4 и посчитай их сумму.
-- expected: 10
WITH RECURSIVE numbers AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n + 1
    FROM numbers
    WHERE n < 4
)
SELECT SUM(n) AS total_sum
FROM numbers;
