# ТЗ: Capstone: SQL Investigation Pack

## Цель
Собрать итоговый пакет SQL-расследований: производительность endpoint, failed runs по релизам, дефекты и data-quality checks.

## Deliverables
- `slow_endpoints(conn)`
- `failed_runs_by_release(conn)`
- `critical_defects(conn)`
- `data_quality_summary(conn)`
- `main()` с итоговым investigation report

## MVP-функции
- `slow_endpoints` - Верни endpoint по убыванию средней latency.
- `failed_runs_by_release` - Верни количество failed runs по релизам.
- `critical_defects` - Верни critical defects.
- `data_quality_summary` - Верни короткую сводку по качеству данных.

## Пример допустимого вывода
```text
slow_endpoints -> ['/payments/refund', '/reports', '/orders', '/login']
failed_runs_by_release -> ['build-101:1', 'build-102:2', 'build-104:1']
critical_defects -> ['Refund 502']
```

## Критерии готовности
- файл запускается без ошибок;
- каждая функция решает отдельную задачу;
- запросы читаются без магии;
- `main()` показывает рабочий demo flow;
- решение использует темы недели.
