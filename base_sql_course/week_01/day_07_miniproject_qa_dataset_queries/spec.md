# ТЗ: Мини-проект: запросы к QA dataset

## Цель
Собрать набор базовых SQL-запросов к небольшому QA dataset и показать, что ты умеешь читать и фильтровать данные.

## Deliverables
- запрос `list_active_users`
- запрос `high_priority_cases`
- запрос `open_task_ids`
- запрос `failed_run_ids`
- демо `qa_dataset_queries.sql` с печатью результатов

## MVP-запросы
- `list_active_users` - Список имён активных пользователей.
- `high_priority_cases` - Список high priority test case.
- `open_task_ids` - Список id открытых задач.
- `failed_run_ids` - Список id failed test runs.

## Пример допустимого вывода
```text
Active users: ['Anna', 'Boris', 'Oleg']
High priority cases: ['Create order', 'Login works']
Open task ids: [1, 4, 5]
Failed run ids: [2, 6]
```

## Критерии готовности
- SQL-скрипт выполняется без ошибок на подготовленном dataset;
- каждый запрос решает одну понятную задачу;
- запросы читаются;
- `qa_dataset_queries.sql` показывает рабочий demo flow.
