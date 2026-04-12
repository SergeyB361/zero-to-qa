# ТЗ: Мини-проект: отчёт с JOIN и агрегациями

## Цель
Собрать маленький SQL-отчёт по тестовым запускам, используя JOIN, GROUP BY и агрегаты.

## Deliverables
- запрос `runs_per_status`
- запрос `avg_duration_per_case`
- запрос `open_defects_by_severity`
- читаемый `metrics_report.sql` с выводом отчёта

## MVP-запросы
- `runs_per_status` - Словарь status -> count.
- `avg_duration_per_case` - Средняя длительность по test case.
- `open_defects_by_severity` - Словарь severity -> count для open defects.

## Пример допустимого вывода
```text
Runs per status: {'failed': 2, 'passed': 3, 'skipped': 1}
Avg duration per case: {'Create order': 57.5, 'Export report': 70.0, 'Filter products': 0.0, 'Login works': 38.0}
Open defects by severity: {'critical': 1, 'minor': 1}
```

## Критерии готовности
- SQL-скрипт выполняется без ошибок на подготовленном dataset;
- каждый запрос решает одну понятную задачу;
- запросы читаются;
- `metrics_report.sql` показывает рабочий demo flow.
