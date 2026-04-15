INSERT INTO users (name, team, is_active, created_at) VALUES
('Anna', 'web', TRUE, '2026-04-01 09:00:00+03'),
('Boris', 'api', TRUE, '2026-04-01 09:10:00+03'),
('Nina', 'mobile', FALSE, '2026-04-01 09:20:00+03'),
('Oleg', 'web', TRUE, '2026-04-01 09:30:00+03');

INSERT INTO projects (name, owner_id, created_at) VALUES
('Web Portal', 1, '2026-04-01 10:00:00+03'),
('Public API', 2, '2026-04-01 10:15:00+03'),
('Mobile App', 3, '2026-04-01 10:30:00+03');

INSERT INTO tasks (project_id, assignee_id, status, priority, estimate_points, closed_at) VALUES
(1, 1, 'open', 'high', 5, NULL),
(1, 4, 'closed', 'medium', 3, '2026-04-03 18:00:00+03'),
(2, 2, 'in_progress', 'critical', 8, NULL),
(3, 3, 'blocked', 'high', 5, NULL);

INSERT INTO test_cases (title, area, priority) VALUES
('Login works', 'auth', 'high'),
('Create order', 'checkout', 'high'),
('Refresh token', 'api', 'critical'),
('Profile update', 'user', 'medium');

INSERT INTO test_runs (case_id, status, executed_by, duration_seconds, executed_at) VALUES
(1, 'passed', 1, 35.0, '2026-04-10 10:00:00+03'),
(2, 'failed', 2, 41.0, '2026-04-10 10:30:00+03'),
(3, 'passed', 2, 55.0, '2026-04-10 11:00:00+03'),
(4, 'blocked', 4, 12.0, '2026-04-10 11:20:00+03');

INSERT INTO defects (title, severity, status, task_id, reported_by, reported_at) VALUES
('Login 500', 'critical', 'open', 2, 1, '2026-04-09 09:00:00+03'),
('Wrong total', 'major', 'fixed', 1, 2, '2026-04-09 11:15:00+03'),
('Refresh loop', 'critical', 'in_progress', 3, 2, '2026-04-09 12:30:00+03');
