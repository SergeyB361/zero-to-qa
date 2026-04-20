-- Практика: performance

-- Задание 1: choose_index_for_lookup
-- Выбери lookup-запрос из dataset и предложи осмысленный индекс.
-- expected: CREATE INDEX + короткий комментарий зачем он нужен
-- lookup by reported_at is common for defect timeline and recent activity windows.
CREATE INDEX IF NOT EXISTS idx_defects_reported_at_perf
ON defects(reported_at);

-- Задание 2: explain_before_after_index
-- На TEMP TABLE покажи план до и после индекса.
-- expected: два EXPLAIN и один CREATE INDEX
DROP TABLE IF EXISTS perf_status_demo;
CREATE TEMP TABLE perf_status_demo AS
SELECT gs AS id,
       CASE WHEN gs % 20 = 0 THEN 'failed' ELSE 'passed' END AS status
FROM generate_series(1, 50000) AS gs;
EXPLAIN
SELECT * FROM perf_status_demo WHERE status = 'failed';
CREATE INDEX idx_perf_status_demo_status ON perf_status_demo(status);
EXPLAIN
SELECT * FROM perf_status_demo WHERE status = 'failed';

-- Задание 3: rewrite_time_filter
-- Перепиши time-filter без DATE(...) в WHERE и добавь EXPLAIN.
-- expected: rewrite через диапазон и EXPLAIN
EXPLAIN
SELECT id
FROM test_runs
WHERE executed_at::date = DATE '2026-04-10';

EXPLAIN
SELECT id
FROM test_runs
WHERE executed_at >= TIMESTAMPTZ '2026-04-10 00:00:00+03'
  AND executed_at < TIMESTAMPTZ '2026-04-11 00:00:00+03';

-- Задание 4: optimize_join_report
-- Возьми join-report по projects/tasks/defects и предложи более лёгкую форму через CTE.
-- expected: rewrite, где detail слой сокращается заранее
WITH active_defects AS (
    SELECT task_id,
           COUNT(*) AS active_defects_count
    FROM defects
    WHERE status IN ('open', 'in_progress')
    GROUP BY task_id
)
SELECT p.name,
       COUNT(t.id) AS total_tasks,
       COALESCE(SUM(ad.active_defects_count), 0) AS active_defects
FROM projects AS p
LEFT JOIN tasks AS t ON t.project_id = p.id
LEFT JOIN active_defects AS ad ON ad.task_id = t.id
GROUP BY p.id, p.name
ORDER BY p.id;

-- Задание 5: performance_reasoning_notes
-- Напиши 3 SQL-комментария: когда нужен индекс, когда нужен rewrite, когда нужен EXPLAIN ANALYZE.
-- expected: 3 коротких осмысленных комментария
-- use index: when stable filters/joins repeatedly touch the same selective columns.
-- use rewrite: when query shape does excess work before filtering or aggregation.
-- use explain analyze: when estimated plan is not enough and real row counts/time matter.
SELECT 'performance reasoning notes completed' AS note;
