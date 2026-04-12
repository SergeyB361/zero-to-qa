# HAVING

## Зачем это нужно
HAVING нужен, когда после `GROUP BY` надо оставить только интересные группы: например только статусы с несколькими запусками или пользователей с несколькими задачами.

## Что нужно понять
- HAVING
- фильтрация агрегатов
- разница между WHERE и HAVING

## Рабочая логика
1. Определи, из каких таблиц ты читаешь данные.
2. Сузь выборку фильтрами.
3. Только потом добавляй сортировку, группировку или join.
4. Проверяй вывод на маленьком наборе данных.

## Примеры
### Пример 1 - Статусы test_runs с количеством больше 1
```sql
SELECT status, COUNT(*) AS run_count FROM test_runs GROUP BY status HAVING COUNT(*) > 1 ORDER BY status;
```

### Пример 2 - Пользователи с более чем одной задачей
```sql
SELECT assignee_id, COUNT(*) AS task_count FROM tasks GROUP BY assignee_id HAVING COUNT(*) > 1;
```

### Пример 3 - Проекты с суммарной оценкой больше 5 часов
```sql
SELECT project_id, SUM(estimate_hours) AS total_estimate FROM tasks GROUP BY project_id HAVING SUM(estimate_hours) > 5;
```

## Типичные ошибки
- использовать HAVING там, где нужен WHERE
- фильтровать сырые строки после группировки

## Практика
В `practice.py` есть функции для самостоятельной реализации:
- `statuses_with_multiple_runs` - Верни статусы test_runs, у которых count > 1.
- `users_with_multiple_tasks` - Верни id пользователей, у которых больше одной задачи.
- `projects_with_large_backlog` - Верни id проектов, у которых сумма estimate_hours >= 10.

## Что дальше
Сначала запусти `examples.py`, затем реализуй функции из `practice.py` и сверь вывод с expected.
