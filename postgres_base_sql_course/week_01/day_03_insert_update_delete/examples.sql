-- INSERT, UPDATE, DELETE
-- Примеры ниже выполняй как единый script: изменения будут откатаны.

BEGIN;

-- Пример 1: вставка новой строки и мгновенная проверка через RETURNING.
INSERT INTO test_cases (title, area, priority)
VALUES ('Reset password', 'auth', 'medium')
RETURNING id, title, priority;

-- Пример 2: обновление задачи и проверка нового состояния.
UPDATE tasks
SET status = 'closed', closed_at = NOW()
WHERE id = 1
RETURNING id, status, closed_at;

-- Пример 3: удаление дефекта и проверка, что именно удалилось.
DELETE FROM defects
WHERE id = 2
RETURNING id, title, status;

ROLLBACK;
