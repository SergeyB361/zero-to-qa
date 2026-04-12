# ТЗ: Мини-проект: аналитические SQL-запросы

## Цель
Собрать набор аналитических запросов поверх test_runs, defects и api_checks с использованием CTE и оконных функций.

## Deliverables
- `slowest_cases(conn)`
- `failed_runs_by_release(conn)`
- `api_latency_ranking(conn)`
- `defect_summary(conn)`
- `main()` с отчётом

## MVP-функции
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
- файл запускается без ошибок;
- каждая функция решает отдельную задачу;
- запросы читаются без магии;
- `main()` показывает рабочий demo flow;
- решение использует темы недели.
