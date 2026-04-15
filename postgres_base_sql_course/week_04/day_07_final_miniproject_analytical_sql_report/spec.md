# ТЗ: Финальный мини-проект — analytical SQL report

## Цель
Собрать компактный набор аналитических SQL-отчётов по проектам, задачам, тестовым запускам и дефектам без использования Python-логики поверх данных.

## Deliverables
- блок `project_load_report`
- блок `run_status_report`
- блок `latest_executor_activity`
- блок `open_defect_severity_report`
- один цельный файл `analytical_sql_report.sql`

## Обязательные требования
- используй dataset из `postgres_lab`;
- каждый отчёт должен решать одну понятную задачу;
- в запросах должны быть читаемые alias;
- в файле должен быть demo flow: короткие комментарии и запросы в логичном порядке;
- минимум в двух местах используй темы `week_04` осознанно, а не формально.

## MVP-идея отчётов
- `project_load_report` — по каждому проекту: total tasks и unfinished tasks.
- `run_status_report` — summary по test_runs с разбивкой по статусам.
- `latest_executor_activity` — последний run по каждому executor.
- `open_defect_severity_report` — severity -> count только для defects со статусами open/in_progress.

## Пример допустимого вывода
```text
Project load: Web Portal = total 2 / unfinished 1
Run status summary: total 4 / passed 2 / failed 1 / blocked 1
Latest executor activity: Boris -> run 3
Open defects by severity: critical = 2
```

## Критерии готовности
- SQL-скрипт выполняется без ошибок на базе `zero_to_qa`;
- каждый отчёт читается отдельно и имеет понятный смысл;
- запросы не требуют внешней Python-логики для получения результата;
- `analytical_sql_report.sql` показывает понятный финальный demo flow.
