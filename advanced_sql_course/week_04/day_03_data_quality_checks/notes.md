# Data quality checks

## Зачем это нужно
В production и аналитике SQL часто используют не только для фич, но и для поиска плохих данных: дубликатов, NULL, невозможных значений.

## Ключевые идеи
- null checks
- duplicate detection
- range checks
- referential sanity

## Практический фокус
Формулируй качество данных как конкретный SQL-вопрос: что считаем плохим состоянием и как его поймать.

## Типичные ошибки
- делать общие слова вместо явного правила
- не определять, какое значение считается invalid

## Практика
В `practice.py` реализуй функции:
- `find_5xx_api_checks` - Верни id api_checks со статусом 5xx.
- `find_duplicate_titles_in_temp_table` - Создай temp таблицу с дублем и верни дублирующийся title.
- `find_open_defects_without_owner` - Верни количество open defects без owner. Ожидается 0.

## Что дальше
Сначала запусти `examples.py`, затем доведи функции из `practice.py` до expected-результатов.
