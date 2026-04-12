# Условные агрегации

## Зачем это нужно
Когда нужны несколько метрик в одном отчёте, условные агрегации часто удобнее набора отдельных запросов.

## Ключевые идеи
- CASE WHEN
- COUNT/SUM по условию
- pivot-like отчёты

## Практический фокус
Это часто используется в QA-дашбордах: passed/failed/skipped по area, open/closed defects по severity.

## Типичные ошибки
- делать по одному запросу на каждую метрику
- путать COUNT и SUM(CASE...)

## Практика
В `practice.sql` реализуй функции:
- `status_counts_per_area` - Верни пары `area:passed:failed`.
- `severity_open_closed` - Верни пары `severity:open:closed`.
- `api_status_buckets` - Верни словарь bucket -> count для api_checks.

## Что дальше
Сначала запусти `examples.sql`, затем доведи функции из `practice.sql` до expected-результатов.
