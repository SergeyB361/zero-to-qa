-- Дата и время в SQL
-- Выполни скрипт целиком в SQLite или другой совместимой среде.

-- Setup dataset
CREATE TABLE test_runs (id INTEGER PRIMARY KEY, status TEXT NOT NULL, executed_at TEXT NOT NULL);
    INSERT INTO test_runs VALUES
        (1, 'passed', '2026-04-01 10:00:00'),
        (2, 'failed', '2026-04-01 12:15:00'),
        (3, 'passed', '2026-04-02 09:40:00');

-- Пример 1
SELECT date(executed_at) AS day, COUNT(*) AS total FROM test_runs GROUP BY date(executed_at) ORDER BY day;

-- Пример 2
SELECT id, strftime('%Y-%m', executed_at) AS month_bucket FROM test_runs ORDER BY id;
