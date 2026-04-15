# ТЗ: Мини-проект — analytics queries

## Цель
Собрать набор Postgres-native аналитических запросов по dataset из `postgres_lab`, используя CTE и оконные функции.

## Deliverables
- блок `latest_executor_runs`
- блок `daily_run_calendar`
- блок `project_points_ranking`
- блок `reporter_defect_summary`
- один SQL-файл `analytics_queries.sql`

## Обязательные требования
- используй dataset из `postgres_lab`;
- минимум один запрос должен использовать обычный CTE;
- минимум один запрос должен использовать recursive CTE;
- минимум два запроса должны использовать window functions или ranking;
- все запросы должны читаться как самостоятельные мини-отчёты.

## MVP-идея
- `latest_executor_runs` — последний run по каждому executor.
- `daily_run_calendar` — календарь на несколько дней с количеством test_runs по каждому дню.
- `project_points_ranking` — ranking проектов по сумме estimate_points.
- `reporter_defect_summary` — defects с количеством дефектов на reporter и читаемым summary.

## Пример допустимого вывода
```text
Latest run: Boris -> run 3
Calendar: 2026-04-10 -> 4
Project ranking: Web Portal -> rank 1
Reporter summary: Boris -> 2 defects
```

## Критерии готовности
- SQL-скрипт выполняется без ошибок на Postgres;
- каждый отчёт имеет понятный смысл;
- advanced-функции используются осознанно, а не формально;
- `analytics_queries.sql` можно читать как цельный demo flow.
