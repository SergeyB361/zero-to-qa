# Views и materialized views

## Зачем это нужно
View помогает скрыть сложность повторяющегося запроса, а materialized view - ещё и экономить вычисления на тяжёлой аналитике.

## Ключевые идеи
- VIEW
- повторное использование SQL
- materialized view как snapshot
- refresh concept

## Практический фокус
В SQLite есть обычные views. Materialized view показываем как идею и через table snapshot.

## Типичные ошибки
- ожидать materialized views в SQLite из коробки
- использовать view там, где лучше обычный запрос в коде

## Практика
В `practice.sql` напиши запросы:
- `create_open_defects_view` - Создай view open_defects_view и верни True, если она появилась.
- `query_open_defects_view` - Верни пары `title:severity` из open_defects_view.
- `build_snapshot_table` - Создай table snapshot по open defects и верни количество строк.

## Что дальше
Сначала выполни `examples.sql`, затем доведи запросы из `practice.sql` до expected-результатов.
