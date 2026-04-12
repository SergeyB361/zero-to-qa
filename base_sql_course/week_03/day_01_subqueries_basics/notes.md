# Подзапросы: база

## Зачем это нужно
Подзапрос помогает сначала вычислить промежуточный результат, а потом использовать его как фильтр или источник данных во внешнем запросе.

## Что нужно понять
- подзапрос в WHERE
- подзапрос в FROM
- агрегат внутри подзапроса

## Рабочая логика
1. Определи, из каких таблиц ты читаешь данные.
2. Сузь выборку фильтрами.
3. Только потом добавляй сортировку, группировку или join.
4. Проверяй вывод на маленьком наборе данных.

## Примеры
### Пример 1 - Задачи длиннее среднего estimate
```sql
SELECT id, estimate_hours FROM tasks WHERE estimate_hours > (SELECT AVG(estimate_hours) FROM tasks) ORDER BY id;
```

### Пример 2 - Test cases с failed runs
```sql
SELECT title FROM test_cases WHERE id IN (SELECT case_id FROM test_runs WHERE status = 'failed') ORDER BY title;
```

### Пример 3 - Пользователи, которые владеют проектами
```sql
SELECT name FROM users WHERE id IN (SELECT owner_id FROM projects) ORDER BY name;
```

## Типичные ошибки
- писать подзапрос там, где проще JOIN
- не понимать, что подзапрос может вернуть одну строку или много строк

## Практика
В `practice.py` есть функции для самостоятельной реализации:
- `tasks_above_average` - Верни id задач, у которых estimate_hours выше среднего по tasks.
- `cases_with_failed_runs` - Верни названия test_cases, у которых были failed runs.
- `owners_of_projects` - Верни имена владельцев проектов.

## Что дальше
Сначала запусти `examples.py`, затем реализуй функции из `practice.py` и сверь вывод с expected.
