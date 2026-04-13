-- Композитные SQL-запросы
-- Выполни setup-часть, затем замени TODO-запросы своими решениями.

-- Setup dataset
CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL, team TEXT NOT NULL);
    CREATE TABLE projects (id INTEGER PRIMARY KEY, name TEXT NOT NULL, owner_id INTEGER NOT NULL, FOREIGN KEY(owner_id) REFERENCES users(id));
    CREATE TABLE tasks (id INTEGER PRIMARY KEY, project_id INTEGER NOT NULL, assignee_id INTEGER NOT NULL, status TEXT NOT NULL, priority TEXT NOT NULL, estimate_hours INTEGER NOT NULL, FOREIGN KEY(project_id) REFERENCES projects(id), FOREIGN KEY(assignee_id) REFERENCES users(id));
    INSERT INTO users VALUES (1, 'Anna', 'web'), (2, 'Boris', 'api'), (3, 'Nina', 'mobile');
    INSERT INTO projects VALUES (1, 'Portal', 1), (2, 'API', 2), (3, 'Mobile', 3);
    INSERT INTO tasks VALUES
        (1, 1, 1, 'open', 'high', 5),
        (2, 1, 1, 'closed', 'low', 2),
        (3, 2, 2, 'open', 'high', 8),
        (4, 2, 1, 'open', 'medium', 3),
        (5, 3, 3, 'open', 'medium', 6);

-- Задание 1: open_tasks_per_project
-- open tasks per project
-- expected: "['API:2', 'Mobile:1', 'Portal:1']"
-- TODO: замени заглушку реальным SQL-запросом
SELECT 'TODO: open_tasks_per_project' AS todo;

-- Задание 2: heavy_projects
-- heavy projects
-- expected: "['API', 'Mobile']"
-- TODO: замени заглушку реальным SQL-запросом
SELECT 'TODO: heavy_projects' AS todo;

-- Задание 3: owners_with_open_work
-- owners with open work
-- expected: "['Anna:1', 'Boris:2', 'Nina:1']"
-- TODO: замени заглушку реальным SQL-запросом
SELECT 'TODO: owners_with_open_work' AS todo;

-- Задание 4: owner_estimate_load
-- Верни суммарную estimate_hours открытых задач по владельцам проектов.
-- expected: "['Anna:5', 'Boris:11', 'Nina:6']"
-- TODO: замени заглушку реальным SQL-запросом
SELECT 'TODO: owner_estimate_load' AS todo;

-- Задание 5: users_with_high_priority_open_tasks
-- Верни имена пользователей, у которых есть open задача с priority = high.
-- expected: "['Anna', 'Boris']"
-- TODO: замени заглушку реальным SQL-запросом
SELECT 'TODO: users_with_high_priority_open_tasks' AS todo;
