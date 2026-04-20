-- Практика: MVCC и visibility

-- Задание 1: txid_current_demo
-- Покажи текущий transaction id.
SELECT txid_current() AS current_txid;

-- Задание 2: xmin_xmax_temp_demo
-- На TEMP TABLE посмотри xmin/xmax до и после UPDATE.
DROP TABLE IF EXISTS mvcc_demo;
CREATE TEMP TABLE mvcc_demo AS
SELECT 1::BIGINT AS id,
       'open'::TEXT AS status;

SELECT xmin, xmax, * FROM mvcc_demo;
UPDATE mvcc_demo
SET status = 'closed'
WHERE id = 1;
SELECT xmin, xmax, * FROM mvcc_demo;

-- Задание 3: snapshot_visibility_comment
-- Кратко объясни snapshot visibility.
SELECT 'MVCC gives each statement or transaction its own visibility snapshot, so readers do not need to block normal writers.' AS note;

-- Задание 4: mvcc_vs_locks_comment
-- Сравни MVCC и locks.
SELECT 'MVCC controls which row versions are visible; locks coordinate conflicting writes and explicit row-level protection such as FOR UPDATE.' AS note;

-- Задание 5: vacuum_reason_comment
-- Объясни, зачем нужен VACUUM.
SELECT 'VACUUM cleans up dead tuples created by UPDATE or DELETE, which keeps table bloat under control and helps planner statistics stay healthy.' AS note;
