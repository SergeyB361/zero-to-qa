-- Практика: views и materialized views

-- Задание 1: create_project_view
-- Создай view с нагрузкой по задачам на проект.
DROP VIEW IF EXISTS project_task_overview_practice;
CREATE VIEW project_task_overview_practice AS
SELECT p.id,
       p.name,
       COUNT(t.id) AS total_tasks,
       COUNT(t.id) FILTER (WHERE t.status <> 'closed') AS unfinished_tasks
FROM projects AS p
LEFT JOIN tasks AS t ON t.project_id = p.id
GROUP BY p.id, p.name;

SELECT * FROM project_task_overview_practice ORDER BY id;

-- Задание 2: create_materialized_defect_view
-- Создай materialized view со snapshot по severity.
DROP MATERIALIZED VIEW IF EXISTS defect_severity_snapshot_practice;
CREATE MATERIALIZED VIEW defect_severity_snapshot_practice AS
SELECT severity,
       COUNT(*) AS defects_count
FROM defects
GROUP BY severity;

SELECT * FROM defect_severity_snapshot_practice ORDER BY severity;

-- Задание 3: refresh_materialized_view
-- Обнови materialized view вручную.
REFRESH MATERIALIZED VIEW defect_severity_snapshot_practice;

-- Задание 4: choose_view_vs_materialized_view
-- Кратко зафиксируй правило выбора.
SELECT 'Use a normal view for always-fresh lightweight logic; use a materialized view for heavier snapshots that can be refreshed on demand.' AS note;

-- Задание 5: cleanup_views
-- Удали учебные объекты после демонстрации.
DROP MATERIALIZED VIEW IF EXISTS defect_severity_snapshot_practice;
DROP VIEW IF EXISTS project_task_overview_practice;
