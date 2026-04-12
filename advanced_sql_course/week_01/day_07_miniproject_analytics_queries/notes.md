# Мини-проект: аналитические SQL-запросы

## Цель
Собрать набор аналитических запросов поверх test_runs, defects и api_checks с использованием CTE и оконных функций.

## Что должно получиться
- `slowest_cases(conn)`
- `failed_runs_by_release(conn)`
- `api_latency_ranking(conn)`
- `defect_summary(conn)`
- `main()` с отчётом

## Как подходить к проекту
1. Запусти starter-файл и посмотри expected demo flow.
2. Реализуй функции по одной.
3. Проверяй, что SQL остаётся читаемым.
4. В конце оформи нормальный `main()`.
