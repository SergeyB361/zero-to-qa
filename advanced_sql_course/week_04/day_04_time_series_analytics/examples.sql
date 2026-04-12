-- Time-series analytics и bucketization
-- Выполни скрипт целиком в SQLite или другой совместимой среде.

-- Setup dataset
CREATE TABLE api_checks (id INTEGER PRIMARY KEY, endpoint TEXT NOT NULL, latency_ms INTEGER NOT NULL, created_at TEXT NOT NULL);
    INSERT INTO api_checks VALUES (1, '/login', 120, '2026-04-01 10:00:00'), (2, '/login', 110, '2026-04-01 12:00:00'), (3, '/orders', 220, '2026-04-02 09:00:00'), (4, '/orders', 180, '2026-04-02 11:00:00');

-- Пример 1
SELECT date(created_at) AS day, ROUND(AVG(latency_ms), 2) AS avg_latency FROM api_checks GROUP BY date(created_at) ORDER BY day;
