# ТЗ: Мини-проект — dataset queries

## Цель
Собрать набор базовых Postgres-запросов к QA dataset из `postgres_lab` и показать, что ты умеешь читать и фильтровать реальные данные без Python-слоя.

## Deliverables
- запрос `list_active_users`
- запрос `high_priority_cases`
- запрос `unfinished_task_ids`
- запрос `failed_run_ids`
- запрос `open_defects`
- demo flow в `dataset_queries.sql`

## MVP-запросы
- `list_active_users` — список имён активных пользователей.
- `high_priority_cases` — список `test_cases` с приоритетом `high` или `critical`.
- `unfinished_task_ids` — список id задач, у которых `status <> 'closed'`.
- `failed_run_ids` — список id `test_runs` со статусом `failed`.
- `open_defects` — список title дефектов со статусом `open` или `in_progress`.

## Пример допустимого вывода
```text
Active users: Anna, Boris, Oleg
High priority cases: Login works, Create order, Refresh token
Unfinished task ids: 1, 3, 4
Failed run ids: 2
Open defects: Login 500, Refresh loop
```

## Критерии готовности
- SQL-скрипт выполняется без ошибок на базе `zero_to_qa`;
- каждый запрос решает одну понятную задачу;
- запросы читаются без устного объяснения;
- `dataset_queries.sql` показывает рабочий demo flow.
