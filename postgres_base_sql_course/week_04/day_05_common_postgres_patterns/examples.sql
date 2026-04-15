-- Common Postgres patterns

-- Пример 1: status summary по test_runs через FILTER.
SELECT COUNT(*) AS total_runs,
       COUNT(*) FILTER (WHERE status = 'passed') AS passed_runs,
       COUNT(*) FILTER (WHERE status = 'failed') AS failed_runs,
       COUNT(*) FILTER (WHERE status = 'blocked') AS blocked_runs
FROM test_runs;

-- Пример 2: последний run по каждому executor через DISTINCT ON.
SELECT DISTINCT ON (executed_by)
       executed_by,
       id AS latest_run_id,
       status,
       executed_at
FROM test_runs
ORDER BY executed_by, executed_at DESC;

-- Пример 3: список defect titles по severity через STRING_AGG.
SELECT severity,
       STRING_AGG(title, ', ' ORDER BY title) AS defect_titles
FROM defects
GROUP BY severity
ORDER BY severity;

-- Пример 4: самый новый пользователь в каждой команде.
SELECT DISTINCT ON (team)
       team,
       id,
       name,
       created_at
FROM users
ORDER BY team, created_at DESC;
