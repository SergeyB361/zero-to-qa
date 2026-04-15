-- Практика: транзакции

-- Задание 1: close_and_rollback_task
-- Напиши транзакцию, которая меняет task id = 1 на closed,
-- затем делает проверочный SELECT и завершает всё через ROLLBACK.
-- expected: после отката финальный status снова open
SELECT 'TODO: close_and_rollback_task' AS todo;

-- Задание 2: temp_insert_and_commit
-- Создай TEMP TABLE, вставь в неё 2 строки внутри транзакции и подтверди COMMIT.
-- expected: итоговый COUNT(*) = 2
SELECT 'TODO: temp_insert_and_commit' AS todo;

-- Задание 3: two_updates_one_rollback
-- На TEMP TABLE balances выполни 2 UPDATE в одной транзакции и затем ROLLBACK.
-- expected: значение возвращается к исходному
SELECT 'TODO: two_updates_one_rollback' AS todo;

-- Задание 4: inspect_before_commit
-- Напиши сценарий: SELECT текущего статуса task id = 3,
-- затем UPDATE внутри транзакции, затем SELECT после изменения,
-- затем ROLLBACK.
-- expected: внутри транзакции status изменился, после ROLLBACK снова in_progress
SELECT 'TODO: inspect_before_commit' AS todo;

-- Задание 5: commit_temp_update
-- Создай TEMP TABLE tx_flags, обнови одну строку внутри транзакции и подтверди COMMIT.
-- expected: финальный flag = false
SELECT 'TODO: commit_temp_update' AS todo;
