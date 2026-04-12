# NULL, LIKE, IN, BETWEEN

## Зачем это нужно
Эти конструкции часто встречаются в QA-проверках: поиск пустых полей, фильтрация по диапазонам и быстрый отбор по нескольким значениям.

## Что нужно понять
- NULL и `IS NULL`
- LIKE
- IN
- BETWEEN
- поиск по диапазону

## Рабочая логика
1. Определи, из каких таблиц ты читаешь данные.
2. Сузь выборку фильтрами.
3. Только потом добавляй сортировку, группировку или join.
4. Проверяй вывод на маленьком наборе данных.

## Примеры
### Пример 1 - Открытые задачи без даты закрытия
```sql
SELECT id, status FROM tasks WHERE closed_at IS NULL ORDER BY id;
```

### Пример 2 - Test cases, начинающиеся на Create
```sql
SELECT title FROM test_cases WHERE title LIKE 'Create%';
```

### Пример 3 - Запуски средней длины
```sql
SELECT id, duration_sec FROM test_runs WHERE duration_sec BETWEEN 35 AND 60 ORDER BY id;
```

## Типичные ошибки
- писать `= NULL` вместо `IS NULL`
- забывать `%` в `LIKE`
- не помнить, что `BETWEEN` включает границы

## Практика
В `practice.py` есть функции для самостоятельной реализации:
- `open_tasks_without_closed_at` - Верни id открытых задач, у которых closed_at пустой.
- `areas_in_list` - Верни названия test case из областей auth и checkout.
- `medium_size_runs` - Верни id test_runs с duration_sec между 35 и 60.

## Что дальше
Сначала запусти `examples.py`, затем реализуй функции из `practice.py` и сверь вывод с expected.
