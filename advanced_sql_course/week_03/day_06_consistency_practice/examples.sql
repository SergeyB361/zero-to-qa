-- Практика на consistency
-- Выполни скрипт целиком в SQLite или другой совместимой среде.

-- Setup dataset
PRAGMA foreign_keys = ON;

        CREATE TABLE qa_engineers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            team TEXT NOT NULL
        );

        CREATE TABLE releases (
            id INTEGER PRIMARY KEY,
            build_tag TEXT NOT NULL,
            branch TEXT NOT NULL,
            deployed_at TEXT NOT NULL
        );

        CREATE TABLE test_cases (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            area TEXT NOT NULL,
            priority TEXT NOT NULL,
            owner_id INTEGER NOT NULL,
            FOREIGN KEY(owner_id) REFERENCES qa_engineers(id)
        );

        CREATE TABLE test_runs (
            id INTEGER PRIMARY KEY,
            case_id INTEGER NOT NULL,
            release_id INTEGER NOT NULL,
            engineer_id INTEGER NOT NULL,
            status TEXT NOT NULL,
            duration_sec INTEGER NOT NULL,
            executed_at TEXT NOT NULL,
            FOREIGN KEY(case_id) REFERENCES test_cases(id),
            FOREIGN KEY(release_id) REFERENCES releases(id),
            FOREIGN KEY(engineer_id) REFERENCES qa_engineers(id)
        );

        CREATE TABLE api_checks (
            id INTEGER PRIMARY KEY,
            release_id INTEGER NOT NULL,
            endpoint TEXT NOT NULL,
            status_code INTEGER NOT NULL,
            response_ms INTEGER NOT NULL,
            created_at TEXT NOT NULL,
            FOREIGN KEY(release_id) REFERENCES releases(id)
        );

        CREATE TABLE defects (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            severity TEXT NOT NULL,
            status TEXT NOT NULL,
            release_id INTEGER NOT NULL,
            owner_id INTEGER NOT NULL,
            created_at TEXT NOT NULL,
            resolved_at TEXT,
            FOREIGN KEY(release_id) REFERENCES releases(id),
            FOREIGN KEY(owner_id) REFERENCES qa_engineers(id)
        );

        CREATE TABLE audit_log (
            id INTEGER PRIMARY KEY,
            entity_type TEXT NOT NULL,
            entity_id INTEGER NOT NULL,
            action TEXT NOT NULL,
            actor_id INTEGER NOT NULL,
            created_at TEXT NOT NULL,
            FOREIGN KEY(actor_id) REFERENCES qa_engineers(id)
        );

        INSERT INTO qa_engineers VALUES
            (1, 'Anna', 'web'),
            (2, 'Boris', 'api'),
            (3, 'Nina', 'mobile'),
            (4, 'Oleg', 'platform');

        INSERT INTO releases VALUES
            (1, 'build-101', 'main', '2026-04-01'),
            (2, 'build-102', 'main', '2026-04-02'),
            (3, 'build-103', 'release', '2026-04-03'),
            (4, 'build-104', 'hotfix', '2026-04-04');

        INSERT INTO test_cases VALUES
            (1, 'Login works', 'auth', 'high', 1),
            (2, 'Create order', 'checkout', 'high', 2),
            (3, 'Refund order', 'payments', 'high', 2),
            (4, 'Filter products', 'catalog', 'medium', 1),
            (5, 'Export report', 'admin', 'low', 4),
            (6, 'Refresh token', 'auth', 'medium', 2);

        INSERT INTO test_runs VALUES
            (1, 1, 1, 1, 'passed', 32, '2026-04-01 10:00:00'),
            (2, 2, 1, 2, 'failed', 55, '2026-04-01 10:10:00'),
            (3, 4, 1, 1, 'passed', 40, '2026-04-01 10:30:00'),
            (4, 1, 2, 2, 'failed', 38, '2026-04-02 11:00:00'),
            (5, 2, 2, 2, 'passed', 52, '2026-04-02 11:15:00'),
            (6, 3, 2, 3, 'failed', 61, '2026-04-02 11:40:00'),
            (7, 6, 3, 2, 'passed', 35, '2026-04-03 09:20:00'),
            (8, 5, 3, 4, 'passed', 75, '2026-04-03 09:45:00'),
            (9, 1, 4, 1, 'passed', 31, '2026-04-04 08:50:00'),
            (10, 3, 4, 3, 'passed', 59, '2026-04-04 09:10:00'),
            (11, 2, 4, 2, 'failed', 58, '2026-04-04 09:30:00');

        INSERT INTO api_checks VALUES
            (1, 1, '/login', 200, 120, '2026-04-01 10:05:00'),
            (2, 1, '/orders', 500, 380, '2026-04-01 10:20:00'),
            (3, 2, '/login', 401, 95, '2026-04-02 11:05:00'),
            (4, 2, '/orders', 200, 210, '2026-04-02 11:25:00'),
            (5, 3, '/reports', 200, 450, '2026-04-03 09:50:00'),
            (6, 4, '/orders', 200, 205, '2026-04-04 09:35:00'),
            (7, 4, '/payments/refund', 502, 510, '2026-04-04 09:40:00');

        INSERT INTO defects VALUES
            (1, 'Login returns 401', 'major', 'open', 2, 2, '2026-04-02', NULL),
            (2, 'Refund 502', 'critical', 'open', 4, 3, '2026-04-04', NULL),
            (3, 'Order total mismatch', 'major', 'closed', 1, 1, '2026-04-01', '2026-04-03'),
            (4, 'Slow export', 'minor', 'open', 3, 4, '2026-04-03', NULL);

        INSERT INTO audit_log VALUES
            (1, 'defect', 1, 'created', 2, '2026-04-02 12:00:00'),
            (2, 'defect', 3, 'closed', 1, '2026-04-03 13:00:00'),
            (3, 'release', 4, 'deployed', 4, '2026-04-04 08:00:00'),
            (4, 'test_run', 11, 'recorded', 2, '2026-04-04 09:31:00');

-- Пример 1
EXPLAIN QUERY PLAN;

-- Пример 2
SELECT COUNT(*) AS cnt FROM audit_log WHERE entity_type = 'defect' AND entity_id = 1;

-- Пример 3
BEGIN;

-- Пример 4
UPDATE defects SET status = 'closed', resolved_at = '2026-04-05' WHERE id = 1;

-- Пример 5
INSERT INTO audit_log (id, entity_type, entity_id, action, actor_id, created_at) VALUES (10, 'defect', 1, 'closed', 2, '2026-04-05 10:00:00');

-- Пример 6
SELECT status, resolved_at FROM defects WHERE id = 1;
