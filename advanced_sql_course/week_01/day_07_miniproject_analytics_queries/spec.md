# ТЗ: Мини-проект: аналитические SQL-запросы

## Цель
Собрать набор аналитических запросов поверх test_runs, defects и api_checks с использованием CTE и оконных функций.

## Deliverables
- запрос `slowest_cases`
- запрос `failed_runs_by_release`
- запрос `api_latency_ranking`
- запрос `defect_summary`
- `analytics_queries.sql` с отчётом

## MVP-запросы
- `slowest_cases` - Top-3 test case по средней длительности.
- `failed_runs_by_release` - Количество failed runs по релизам.
- `api_latency_ranking` - Ранжирование endpoint по средней latency.
- `defect_summary` - Короткий отчёт по дефектам.

## Пример допустимого вывода
```text
slowest_cases -> ['Export report', 'Refund order', 'Create order']
failed_runs_by_release -> ['build-101:1', 'build-102:2', 'build-104:1']
api_latency_ranking -> ['/payments/refund:1', '/reports:2', '/orders:3', '/login:4']
```

## Критерии готовности
- SQL-скрипт выполняется без ошибок на подготовленном dataset;
- каждый запрос решает отдельную задачу;
- запросы читаются без магии;
- `analytics_queries.sql` показывает рабочий demo flow;
- решение использует темы недели.
