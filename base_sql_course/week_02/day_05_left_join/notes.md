# LEFT JOIN

## Зачем это нужно
LEFT JOIN нужен, когда важно сохранить строки из левой таблицы даже при отсутствии связанных данных. Это типичный паттерн для QA-отчётов и поиска пропусков.

## Что нужно понять
- LEFT JOIN
- строки без совпадений
- поиск отсутствующих данных

## Рабочая логика
1. Определи, из каких таблиц ты читаешь данные.
2. Сузь выборку фильтрами.
3. Только потом добавляй сортировку, группировку или join.
4. Проверяй вывод на маленьком наборе данных.

## Примеры
### Пример 1 - Проекты и количество задач
```sql
SELECT p.name, COUNT(t.id) AS task_count FROM projects AS p LEFT JOIN tasks AS t ON p.id = t.project_id GROUP BY p.id, p.name ORDER BY p.id;
```

### Пример 2 - Test cases и количество запусков
```sql
SELECT c.title, COUNT(r.id) AS run_count FROM test_cases AS c LEFT JOIN test_runs AS r ON c.id = r.case_id GROUP BY c.id, c.title ORDER BY c.id;
```

### Пример 3 - Пользователи и количество найденных дефектов
```sql
SELECT u.name, COUNT(d.id) AS defect_count FROM users AS u LEFT JOIN defects AS d ON u.id = d.created_by GROUP BY u.id, u.name ORDER BY u.id;
```

## Типичные ошибки
- ставить фильтр на правую таблицу в WHERE и случайно превращать LEFT JOIN в INNER JOIN
- не проверять NULL после join

## Практика
В `practice.py` есть функции для самостоятельной реализации:
- `projects_with_task_counts` - Верни пары `project:count` для проектов.
- `users_with_defect_counts` - Верни пары `user:count` для количества созданных дефектов.
- `cases_with_run_counts` - Верни пары `case:count` для количества запусков.

## Что дальше
Сначала запусти `examples.py`, затем реализуй функции из `practice.py` и сверь вывод с expected.
