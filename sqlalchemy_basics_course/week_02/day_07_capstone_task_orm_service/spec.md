# Task ORM Service — Spec

Нужно реализовать:
1. модели `Task` и `TaskComment`
2. one-to-many связь между ними
3. `seed_tasks(session)`
4. `add_comment(session, task_id, text)`
5. `task_summary(session, task_id)`

Ожидаемый smoke-flow:
- seeded task существует
- новый comment добавляется и коммитится
- summary показывает task title и список comment texts
