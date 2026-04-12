# GROUP BY

## Зачем это нужно
Когда нужна статистика не по всей таблице, а по группам: по статусам, командам, областям тестирования.

## Что нужно понять
- GROUP BY
- агрегация по группам
- сочетание с COUNT/SUM/AVG

## Рабочая логика
1. Определи, из каких таблиц ты читаешь данные.
2. Сузь выборку фильтрами.
3. Только потом добавляй сортировку, группировку или join.
4. Проверяй вывод на маленьком наборе данных.

## Примеры
### Пример 1 - Количество пользователей по командам
```sql
SELECT team, COUNT(*) AS user_count FROM users GROUP BY team ORDER BY team;
```

### Пример 2 - Количество test_runs по статусу
```sql
SELECT status, COUNT(*) AS run_count FROM test_runs GROUP BY status ORDER BY status;
```

### Пример 3 - Средняя оценка задач по статусу
```sql
SELECT status, AVG(estimate_hours) AS avg_estimate FROM tasks GROUP BY status ORDER BY status;
```

## Типичные ошибки
- выбирать колонку, которая не входит в GROUP BY и не агрегируется
- не понимать, что каждая группа превращается в одну строку

## Практика
В `practice.py` есть функции для самостоятельной реализации:
- `runs_per_status` - Верни словарь status -> count для test_runs.
- `tasks_per_priority` - Верни словарь priority -> count для tasks.
- `cases_per_area` - Верни словарь area -> count для test_cases.

## Что дальше
Сначала запусти `examples.py`, затем реализуй функции из `practice.py` и сверь вывод с expected.
