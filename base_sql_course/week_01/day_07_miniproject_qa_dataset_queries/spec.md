# ТЗ: Мини-проект: запросы к QA dataset

## Цель
Собрать набор базовых SQL-запросов к небольшому QA dataset и показать, что ты умеешь читать и фильтровать данные.

## Deliverables
- функция `list_active_users(conn)`
- функция `high_priority_cases(conn)`
- функция `open_task_ids(conn)`
- функция `failed_run_ids(conn)`
- демо `main()` с печатью результатов

## Функции MVP
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
- файл запускается без ошибок;
- каждая функция решает одну понятную задачу;
- запросы читаются;
- `main()` показывает рабочий demo flow.
