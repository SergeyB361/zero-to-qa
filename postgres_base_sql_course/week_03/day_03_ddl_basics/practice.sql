-- Практика: DDL basics

-- Задание 1: create_environments_table
-- Напиши CREATE TABLE environments с колонками:
-- id identity primary key, name text not null, base_url text not null, is_active boolean not null default true.
SELECT 'TODO: create_environments_table' AS todo;

-- Задание 2: alter_environments_add_owner
-- Напиши ALTER TABLE, который добавляет колонку owner_name TEXT в environments.
SELECT 'TODO: alter_environments_add_owner' AS todo;

-- Задание 3: create_releases_table
-- Напиши CREATE TABLE releases с id identity, version text not null, released_at date.
SELECT 'TODO: create_releases_table' AS todo;

-- Задание 4: drop_temp_audit_log
-- Напиши DROP TABLE IF EXISTS temp_audit_log.
SELECT 'TODO: drop_temp_audit_log' AS todo;

-- Задание 5: create_service_health_table
-- Напиши CREATE TABLE service_health с id identity, service_name text not null, status text not null.
SELECT 'TODO: create_service_health_table' AS todo;
