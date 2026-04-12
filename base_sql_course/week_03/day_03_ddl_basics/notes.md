# DDL: CREATE, ALTER, DROP

## Зачем это нужно
DDL - это управление схемой данных. QA и backend-инженеру важно уметь читать такие изменения и делать маленькие технические таблицы для локальной практики.

## Что нужно понять
- CREATE TABLE
- ALTER TABLE
- DROP TABLE
- schema migration basics

## Рабочая логика
1. Определи, из каких таблиц ты читаешь данные.
2. Сузь выборку фильтрами.
3. Только потом добавляй сортировку, группировку или join.
4. Проверяй вывод на маленьком наборе данных.

## Примеры
### Пример 1 - Создать таблицу releases
```sql
CREATE TABLE releases (id INTEGER PRIMARY KEY, version TEXT NOT NULL);
```

### Пример 2 - Добавить колонку released_at
```sql
ALTER TABLE releases ADD COLUMN released_at TEXT;
```

### Пример 3 - Удалить временную таблицу
```sql
DROP TABLE IF EXISTS temp_results;
```

## Типичные ошибки
- путать изменение схемы и изменение данных
- дропать таблицу без проверки
- не смотреть итоговую схему после ALTER

## Практика
В `practice.py` есть функции для самостоятельной реализации:
- `create_releases_table` - Создай таблицу releases и верни True, если она появилась.
- `add_released_at_column` - Добавь колонку released_at и верни список колонок таблицы releases.
- `drop_temp_table` - Создай и затем удали temp_results. Верни True, если таблицы больше нет.

## Что дальше
Сначала запусти `examples.py`, затем реализуй функции из `practice.py` и сверь вывод с expected.
