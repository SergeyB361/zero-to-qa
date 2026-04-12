# Window functions: база

## Зачем это нужно
Window functions позволяют считать агрегаты по группе, не схлопывая строки. Это даёт аналитику поверх детальных данных.

## Ключевые идеи
- OVER()
- PARTITION BY
- оконная функция vs GROUP BY
- агрегаты по окну

## Практический фокус
Используй окно, когда нужно сохранить каждую строку и одновременно видеть контекст: среднее по area, общее число прогонов по release и т.д.

## Типичные ошибки
- путать GROUP BY и OVER()
- не понимать рамку окна
- агрегировать там, где нужна строка-источник

## Практика
В `practice.sql` напиши запросы:
- `avg_duration_per_area_window` - Верни пары `title:avg_area_duration`.
- `runs_per_release_window` - Верни пары `run_id:release_run_count`.
- `max_duration_per_engineer` - Верни пары `run_id:max_engineer_duration`.

## Что дальше
Сначала выполни `examples.sql`, затем доведи запросы из `practice.sql` до expected-результатов.
