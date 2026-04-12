# INNER JOIN

## Зачем это нужно
JOIN - обязательная база для реальной работы. Без него нельзя собрать данные из связанных таблиц: задача + исполнитель, test run + test case, проект + владелец.

## Что нужно понять
- INNER JOIN
- ключ связи
- один-ко-многим
- объединение данных из двух таблиц

## Рабочая логика
1. Определи, из каких таблиц ты читаешь данные.
2. Сузь выборку фильтрами.
3. Только потом добавляй сортировку, группировку или join.
4. Проверяй вывод на маленьком наборе данных.

## Примеры
### Пример 1 - Задачи вместе с именем исполнителя
```sql
SELECT t.id, u.name, t.status FROM tasks AS t INNER JOIN users AS u ON t.assignee_id = u.id ORDER BY t.id;
```

### Пример 2 - Проекты вместе с владельцем
```sql
SELECT p.name, u.name AS owner_name FROM projects AS p INNER JOIN users AS u ON p.owner_id = u.id ORDER BY p.id;
```

### Пример 3 - Запуски тестов вместе с названием test case
```sql
SELECT r.id, c.title, r.status FROM test_runs AS r INNER JOIN test_cases AS c ON r.case_id = c.id ORDER BY r.id;
```

## Типичные ошибки
- соединять не по тем ключам
- получать дубликаты из-за неправильной связи
- не давать alias таблицам в длинных запросах

## Практика
В `practice.py` есть функции для самостоятельной реализации:
- `task_assignees` - Верни пары `task_id:name` для всех задач.
- `project_owners` - Верни пары `project_name:owner_name`.
- `failed_case_titles` - Верни названия test case, у которых были failed runs.

## Что дальше
Сначала запусти `examples.py`, затем реализуй функции из `practice.py` и сверь вывод с expected.
