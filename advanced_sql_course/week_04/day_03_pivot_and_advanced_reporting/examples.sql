-- Pivot-like отчёты и advanced reporting
-- Выполни скрипт целиком в SQLite или другой совместимой среде.

-- Setup dataset
CREATE TABLE defects (id INTEGER PRIMARY KEY, team TEXT NOT NULL, severity TEXT NOT NULL);
    INSERT INTO defects VALUES (1, 'web', 'critical'), (2, 'web', 'major'), (3, 'api', 'major'), (4, 'api', 'major'), (5, 'mobile', 'minor');

-- Пример 1
SELECT team,
               SUM(CASE WHEN severity = 'critical' THEN 1 ELSE 0 END) AS critical_count,
               SUM(CASE WHEN severity = 'major' THEN 1 ELSE 0 END) AS major_count,
               SUM(CASE WHEN severity = 'minor' THEN 1 ELSE 0 END) AS minor_count
        FROM defects
        GROUP BY team
        ORDER BY team;
