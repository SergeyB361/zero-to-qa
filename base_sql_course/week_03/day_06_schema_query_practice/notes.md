# Практика: схема и запросы

## Зачем это нужно
Этот день нужен, чтобы соединить схему, ключи, DDL и запросы. Это уже похоже на реальную работу с БД, а не на изолированные упражнения.

## Что нужно понять
- схема + данные
- join по ключам
- inspection таблиц
- маленькие технические миграции

## Рабочая логика
1. Определи, из каких таблиц ты читаешь данные.
2. Сузь выборку фильтрами.
3. Только потом добавляй сортировку, группировку или join.
4. Проверяй вывод на маленьком наборе данных.

## Примеры
### Пример 1 - Получить список колонок таблицы tasks
```sql
PRAGMA table_info('tasks');
```

### Пример 2 - Test cases без Login в названии
```sql
SELECT title FROM test_cases WHERE title NOT LIKE '%Login%' ORDER BY title;
```

### Пример 3 - Собрать задачи с проектом и исполнителем
```sql
SELECT t.id, p.name AS project_name, u.name AS assignee FROM tasks AS t JOIN projects AS p ON p.id = t.project_id JOIN users AS u ON u.id = t.assignee_id ORDER BY t.id;
```

## Типичные ошибки
- сосредоточиться только на SQL-тексте и не смотреть на модель данных

## Практика
В `practice.py` есть функции для самостоятельной реализации:
- `tasks_column_names` - Верни названия колонок таблицы tasks.
- `joined_task_rows` - Верни количество строк в join tasks + projects + users.
- `create_and_use_temp_table` - Создай temp таблицу qa_notes, вставь 2 строки и верни их количество.

## Что дальше
Сначала запусти `examples.py`, затем реализуй функции из `practice.py` и сверь вывод с expected.
