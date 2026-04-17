-- Практика на consistency
SELECT con.conname,
       pg_get_constraintdef(con.oid)
FROM pg_constraint AS con
JOIN pg_class AS rel ON rel.oid = con.conrelid
WHERE rel.relname = 'defects'
ORDER BY con.conname;

SHOW transaction_isolation;
