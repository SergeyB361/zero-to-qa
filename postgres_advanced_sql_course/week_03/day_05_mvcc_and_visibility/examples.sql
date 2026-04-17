-- MVCC и visibility
CREATE TEMP TABLE mvcc_demo AS
SELECT 1::BIGINT AS id, 'open'::TEXT AS status;

SELECT xmin, xmax, * FROM mvcc_demo;
UPDATE mvcc_demo SET status = 'closed' WHERE id = 1;
SELECT xmin, xmax, * FROM mvcc_demo;
SELECT txid_current() AS current_txid;
