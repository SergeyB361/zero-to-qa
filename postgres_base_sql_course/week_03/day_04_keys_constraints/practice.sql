-- Практика: ключи и constraints

-- Задание 1: define_primary_key
-- Напиши CREATE TABLE teams с PRIMARY KEY по id.
SELECT 'TODO: define_primary_key' AS todo;

-- Задание 2: define_foreign_key
-- Напиши CREATE TABLE team_members, где team_id REFERENCES teams(id).
SELECT 'TODO: define_foreign_key' AS todo;

-- Задание 3: add_unique_constraint
-- Напиши CREATE TABLE qa_users, где email TEXT UNIQUE NOT NULL.
SELECT 'TODO: add_unique_constraint' AS todo;

-- Задание 4: add_check_constraint
-- Напиши CREATE TABLE incidents с CHECK по severity IN (''low'', ''medium'', ''high'').
SELECT 'TODO: add_check_constraint' AS todo;

-- Задание 5: combine_constraints
-- Напиши CREATE TABLE releases с identity id, version TEXT UNIQUE NOT NULL и deployed_at TIMESTAMPTZ.
SELECT 'TODO: combine_constraints' AS todo;
