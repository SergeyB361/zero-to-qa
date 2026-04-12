# SQL для backend и API-анализа

## Зачем это нужно
Backend-команды часто хотят SQL-ответы на практические вопросы: какие endpoint медленные, на каком релизе выросли ошибки, где деградация.

## Ключевые идеи
- latency analysis
- status code distribution
- release correlation
- incident support queries

## Практический фокус
Думай в терминах инженерных вопросов, а не абстрактных таблиц.

## Типичные ошибки
- строить отчёт, который красивый, но бесполезный для incident analysis

## Практика
В `practice.py` реализуй функции:
- `slow_endpoints` - Верни endpoint по убыванию средней latency.
- `error_rate_by_release` - Верни пары `build_tag:error_count` по api_checks со статусом >= 400.
- `critical_defects_by_release` - Верни build_tag для релизов с critical defect.

## Что дальше
Сначала запусти `examples.py`, затем доведи функции из `practice.py` до expected-результатов.
