# ТЗ: Мини-проект — metrics report

## Цель
Собрать маленький SQL-отчёт по QA dataset, используя `JOIN`, `GROUP BY`, агрегаты и читаемые aliases.

## Deliverables
- запрос `runs_per_status`
- запрос `avg_duration_per_case`
- запрос `tasks_per_project`
- запрос `open_defects_by_severity`
- demo flow в `metrics_report.sql`

## MVP-запросы
- `runs_per_status` — словарь `status -> count` по `test_runs`.
- `avg_duration_per_case` — средняя длительность по `test_cases`.
- `tasks_per_project` — число задач по проектам.
- `open_defects_by_severity` — словарь `severity -> count` для дефектов со статусом `open` или `in_progress`.

## Пример допустимого вывода
```text
Runs per status: blocked=1, failed=1, passed=2
Avg duration per case: Create order=41.0, Login works=35.0, Profile update=12.0, Refresh token=55.0
Tasks per project: Mobile App=1, Public API=1, Web Portal=2
Open defects by severity: critical=2
```

## Критерии готовности
- SQL-скрипт выполняется без ошибок на базе `zero_to_qa`;
- каждый запрос решает одну понятную задачу;
- запросы читаются и имеют понятные alias;
- `metrics_report.sql` показывает рабочий demo flow.
