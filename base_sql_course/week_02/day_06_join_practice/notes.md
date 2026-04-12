# Практика на JOIN и агрегации

## Зачем это нужно
Этот день нужен, чтобы перестать делить темы в голове: в реальных запросах JOIN почти всегда идёт вместе с фильтрацией, группировкой и агрегатами.

## Что нужно понять
- JOIN + GROUP BY
- JOIN + HAVING
- чтение условий отчёта

## Рабочая логика
1. Определи, из каких таблиц ты читаешь данные.
2. Сузь выборку фильтрами.
3. Только потом добавляй сортировку, группировку или join.
4. Проверяй вывод на маленьком наборе данных.

## Примеры
### Пример 1 - Средняя длительность runs по test case
```sql
SELECT c.title, AVG(r.duration_sec) AS avg_duration FROM test_cases AS c INNER JOIN test_runs AS r ON c.id = r.case_id GROUP BY c.id, c.title ORDER BY avg_duration DESC;
```

### Пример 2 - Количество задач по исполнителям
```sql
SELECT u.name, COUNT(t.id) AS task_count FROM users AS u LEFT JOIN tasks AS t ON u.id = t.assignee_id GROUP BY u.id, u.name ORDER BY task_count DESC, u.name;
```

### Пример 3 - Проекты с количеством high priority задач
```sql
SELECT p.name, COUNT(t.id) AS high_count FROM projects AS p LEFT JOIN tasks AS t ON p.id = t.project_id AND t.priority = 'high' GROUP BY p.id, p.name ORDER BY p.id;
```

## Типичные ошибки
- делать join правильно, но агрегировать не ту колонку
- забывать сортировку итогового отчёта

## Практика
В `practice.py` есть функции для самостоятельной реализации:
- `avg_duration_per_case` - Верни пары `case:avg_duration`.
- `task_count_per_user` - Верни пары `user:count` по количеству задач.
- `projects_with_high_tasks` - Верни пары `project:high_priority_count`.

## Что дальше
Сначала запусти `examples.py`, затем реализуй функции из `practice.py` и сверь вывод с expected.
