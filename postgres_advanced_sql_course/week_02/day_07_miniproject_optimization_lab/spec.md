# ТЗ: Мини-проект — optimization lab

## Цель
Собрать набор небольших performance-кейсов на Postgres dataset из `postgres_lab` и показать осмысленные способы оптимизации.

## Deliverables
- блок `lookup_case`
- блок `join_case`
- блок `time_filter_case`
- блок `anti_pattern_case`
- один SQL-файл `optimization_lab.sql`

## Обязательные требования
- используй dataset из `postgres_lab` и при необходимости TEMP TABLE для масштабируемого примера;
- в каждом кейсе должен быть baseline-запрос;
- в каждом кейсе должен быть `EXPLAIN` или `EXPLAIN ANALYZE`;
- минимум в двух кейсах должен быть реальный rewrite или индекс;
- в файле должен быть читаемый demo flow.

## MVP-идея
- `lookup_case` — поиск по колонке до и после индекса.
- `join_case` — наивный join-report и более аккуратный вариант через pre-aggregation.
- `time_filter_case` — функция на timestamp vs диапазон времени.
- `anti_pattern_case` — `SELECT *` / `DISTINCT`-костыль / correlated subquery и более чистый rewrite.

## Пример допустимого вывода
```text
Lookup case: index added
Join case: pre-aggregation applied
Time filter case: range filter used
Anti-pattern case: EXISTS replaced DISTINCT
```

## Критерии готовности
- SQL-скрипт выполняется без ошибок на Postgres;
- каждый кейс имеет понятный baseline и improved version;
- performance-выводы привязаны к плану, а не к догадкам;
- `optimization_lab.sql` можно читать как цельную lab-сессию.
