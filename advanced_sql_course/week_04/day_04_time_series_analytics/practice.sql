-- Time-series analytics и bucketization
-- Выполни setup-часть, затем замени TODO-запросы своими решениями.

-- Setup dataset
CREATE TABLE api_checks (id INTEGER PRIMARY KEY, endpoint TEXT NOT NULL, latency_ms INTEGER NOT NULL, status_code INTEGER NOT NULL, created_at TEXT NOT NULL);
    INSERT INTO api_checks VALUES (1, '/login', 120, 200, '2026-04-01 10:00:00'), (2, '/login', 90, 401, '2026-04-01 12:00:00'), (3, '/orders', 220, 200, '2026-04-02 09:00:00'), (4, '/orders', 180, 500, '2026-04-02 11:00:00'), (5, '/reports', 450, 200, '2026-04-03 08:00:00');

-- Задание 1: avg_latency_per_day
-- avg latency per day
-- expected: "['2026-04-01:105.0', '2026-04-02:200.0', '2026-04-03:450.0']"
-- TODO: замени заглушку реальным SQL-запросом
SELECT 'TODO: avg_latency_per_day' AS todo;

-- Задание 2: failing_checks_per_day
-- failing checks per day
-- expected: "['2026-04-01:1', '2026-04-02:1']"
-- TODO: замени заглушку реальным SQL-запросом
SELECT 'TODO: failing_checks_per_day' AS todo;
