-- NULL, LIKE, ILIKE, IN, BETWEEN

-- Пример 1: задачи без даты закрытия.
SELECT id, status, closed_at
FROM tasks
WHERE closed_at IS NULL
ORDER BY id;

-- Пример 2: поиск дефекта по шаблону без учёта регистра.
SELECT id, title
FROM defects
WHERE title ILIKE '%login%';

-- Пример 3: test runs в диапазоне длительности.
SELECT id, status, duration_seconds
FROM test_runs
WHERE duration_seconds BETWEEN 30 AND 50
ORDER BY duration_seconds;

-- Пример 4: задачи со статусом из нескольких значений.
SELECT id, status, priority
FROM tasks
WHERE status IN ('open', 'blocked')
ORDER BY id;
