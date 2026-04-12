# Мини-проект: Query Optimization Lab

## Цель
Собрать набор простых performance-исследований: план до индекса, план после индекса, и небольшие rewrite-примеры.

## Что должно получиться
- `plan_for_failed_runs(conn)`
- `plan_for_orders_endpoint(conn)`
- `add_indexes(conn)`
- `slow_endpoints(conn)`
- `main()` с выводом before/after

## Как подходить к проекту
1. Запусти starter-файл и посмотри expected demo flow.
2. Реализуй функции по одной.
3. Проверяй, что SQL остаётся читаемым.
4. В конце оформи нормальный `main()`.
