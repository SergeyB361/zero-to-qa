# ТЗ: Мини-проект: Query Optimization Lab

## Цель
Собрать набор простых performance-исследований: план до индекса, план после индекса, и небольшие rewrite-примеры.

## Deliverables
- `plan_for_failed_runs(conn)`
- `plan_for_orders_endpoint(conn)`
- `add_indexes(conn)`
- `slow_endpoints(conn)`
- `main()` с выводом before/after

## MVP-функции
- `plan_for_failed_runs` - Верни план для выборки failed runs.
- `plan_for_orders_endpoint` - Верни план для `/orders`.
- `add_indexes` - Создай нужные индексы.
- `slow_endpoints` - Верни endpoint по убыванию средней latency.

## Пример допустимого вывода
```text
plan_for_failed_runs -> plan text
plan_for_orders_endpoint -> plan text
slow_endpoints -> ['/payments/refund', '/reports', '/orders', '/login']
```

## Критерии готовности
- файл запускается без ошибок;
- каждая функция решает отдельную задачу;
- запросы читаются без магии;
- `main()` показывает рабочий demo flow;
- решение использует темы недели.
