-- Postgres setup и инструменты
-- Запуск:
-- psql -h localhost -U postgres -d zero_to_qa -f examples.sql

-- Пример 1: проверить, к какой базе и под каким пользователем ты подключён.
SELECT current_database() AS db_name,
       current_user AS db_user,
       current_schema() AS schema_name;

-- Пример 2: посмотреть список таблиц в public.
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
ORDER BY table_name;

-- Пример 3: посмотреть структуру таблицы users.
SELECT column_name, data_type, is_nullable
FROM information_schema.columns
WHERE table_schema = 'public' AND table_name = 'users'
ORDER BY ordinal_position;

-- Пример 4: убедиться, что seed-данные загрузились.
SELECT id, name, team, is_active
FROM users
ORDER BY id
LIMIT 3;
