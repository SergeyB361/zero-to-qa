# ТЗ: Мини-проект: Query Optimization Lab

## Цель
Собрать набор простых performance-исследований: план до индекса, план после индекса, и небольшие rewrite-примеры.

## Deliverables
- запрос `plan_for_failed_runs`
- запрос `plan_for_orders_endpoint`
- запрос `add_indexes`
- запрос `slow_endpoints`
- `query_optimization_lab.sql` с выводом before/after

## MVP-запросы
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
- SQL-скрипт выполняется без ошибок на подготовленном dataset;
- каждый запрос решает отдельную задачу;
- запросы читаются без магии;
- `query_optimization_lab.sql` показывает рабочий demo flow;
- решение использует темы недели.
