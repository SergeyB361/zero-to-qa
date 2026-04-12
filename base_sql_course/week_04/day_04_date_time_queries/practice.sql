-- Дата и время в SQL
-- Выполни setup-часть, затем замени TODO-запросы своими решениями.

-- Setup dataset
CREATE TABLE api_events (id INTEGER PRIMARY KEY, endpoint TEXT NOT NULL, created_at TEXT NOT NULL);
    INSERT INTO api_events VALUES
        (1, '/login', '2026-04-01 10:00:00'),
        (2, '/orders', '2026-04-01 11:10:00'),
        (3, '/login', '2026-04-02 08:50:00'),
        (4, '/reports', '2026-04-02 09:20:00');

-- Задание 1: events_per_day
-- events per day
-- expected: "['2026-04-01:2', '2026-04-02:2']"
-- TODO: замени заглушку реальным SQL-запросом
SELECT 'TODO: events_per_day' AS todo;

-- Задание 2: month_buckets
-- month buckets
-- expected: "['2026-04', '2026-04', '2026-04', '2026-04']"
-- TODO: замени заглушку реальным SQL-запросом
SELECT 'TODO: month_buckets' AS todo;

-- Задание 3: next_day_after_first_event
-- next day after first event
-- expected: '2026-04-02'
-- TODO: замени заглушку реальным SQL-запросом
SELECT 'TODO: next_day_after_first_event' AS todo;
