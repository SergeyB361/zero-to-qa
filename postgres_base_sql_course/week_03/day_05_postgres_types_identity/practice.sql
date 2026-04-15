-- Практика: Postgres types и identity columns

-- Задание 1: typed_table_for_incidents
-- Напиши CREATE TABLE incidents с колонками:
-- id identity, title text, severity text, is_open boolean, created_at timestamptz.
SELECT 'TODO: typed_table_for_incidents' AS todo;

-- Задание 2: numeric_metric_table
-- Напиши CREATE TABLE quality_metrics с колонками id identity, metric_name text, metric_value numeric(10, 2).
SELECT 'TODO: numeric_metric_table' AS todo;

-- Задание 3: date_vs_timestamp_table
-- Напиши CREATE TABLE releases_calendar с release_date date и created_at timestamptz.
SELECT 'TODO: date_vs_timestamp_table' AS todo;

-- Задание 4: insert_without_manual_id
-- Напиши INSERT в таблицу с identity id без передачи id вручную.
SELECT 'TODO: insert_without_manual_id' AS todo;

-- Задание 5: cast_timestamp_to_text
-- Напиши SELECT с приведением closed_at::text из tasks.
SELECT 'TODO: cast_timestamp_to_text' AS todo;
