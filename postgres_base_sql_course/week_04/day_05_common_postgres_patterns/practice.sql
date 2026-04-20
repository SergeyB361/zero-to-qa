-- Практика: common Postgres patterns

-- Задание 1: run_status_summary_with_filter
-- Посчитай total, passed, failed и blocked test_runs через FILTER.
-- expected: total = 4, passed = 2, failed = 1, blocked = 1
SELECT COUNT(*) AS total_runs,
       COUNT(*) FILTER (WHERE status = 'passed') AS passed_runs,
       COUNT(*) FILTER (WHERE status = 'failed') AS failed_runs,
       COUNT(*) FILTER (WHERE status = 'blocked') AS blocked_runs
FROM test_runs;

-- Задание 2: latest_run_per_executor
-- Верни последний run по каждому executor через DISTINCT ON.
-- expected: Anna -> 1, Boris -> 3, Oleg -> 4
SELECT DISTINCT ON (u.id)
       u.name,
       r.id AS latest_run_id,
       r.executed_at
FROM test_runs AS r
JOIN users AS u ON u.id = r.executed_by
ORDER BY u.id, r.executed_at DESC, r.id DESC;

-- Задание 3: defect_titles_by_severity
-- Собери STRING_AGG(title, ', ' ORDER BY title) по severity.
-- expected: critical -> Login 500, Refresh loop; major -> Wrong total
SELECT severity,
       STRING_AGG(title, ', ' ORDER BY title) AS defect_titles
FROM defects
GROUP BY severity
ORDER BY severity;

-- Задание 4: newest_user_per_team
-- Через DISTINCT ON верни самого нового пользователя в каждой team.
-- expected: api -> Boris, mobile -> Nina, web -> Oleg
SELECT DISTINCT ON (team)
       team,
       name,
       created_at
FROM users
ORDER BY team, created_at DESC, id DESC;

-- Задание 5: active_user_names_by_team
-- Для активных пользователей собери STRING_AGG(name, ', ' ORDER BY name) по team.
-- expected: api -> Boris; web -> Anna, Oleg
SELECT team,
       STRING_AGG(name, ', ' ORDER BY name) AS active_user_names
FROM users
WHERE is_active = TRUE
GROUP BY team
ORDER BY team;
