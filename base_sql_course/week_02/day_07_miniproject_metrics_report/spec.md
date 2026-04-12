# ТЗ: Мини-проект: отчёт с JOIN и агрегациями

## Цель
Собрать маленький SQL-отчёт по тестовым запускам, используя JOIN, GROUP BY и агрегаты.

## Deliverables
- функция `runs_per_status(conn)`
- функция `avg_duration_per_case(conn)`
- функция `open_defects_by_severity(conn)`
- читаемый `main()` с выводом отчёта

## Функции MVP
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
- файл запускается без ошибок;
- каждая функция решает одну понятную задачу;
- запросы читаются;
- `main()` показывает рабочий demo flow.
