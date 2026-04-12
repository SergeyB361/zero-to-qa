# Проверки БД в тестах

## Зачем это нужно
Иногда API/UI-тест проходит только наполовину: ответ пришёл, но данные в БД записались не так. Поэтому нужны прямые DB checks.

## Что нужно понять
- db assertion
- precondition/postcondition
- row exists
- count check

## Рабочая логика
1. Определи, из каких таблиц ты читаешь данные.
2. Сузь выборку фильтрами.
3. Только потом добавляй сортировку, группировку или join.
4. Проверяй вывод на маленьком наборе данных.

## Примеры
### Пример 1 - Проверить, что critical defect существует
```sql
SELECT COUNT(*) FROM defects WHERE severity = 'critical';
```

### Пример 2 - Проверить количество failed runs
```sql
SELECT COUNT(*) FROM test_runs WHERE status = 'failed';
```

### Пример 3 - Проверить, что open задач больше нуля
```sql
SELECT COUNT(*) FROM tasks WHERE status = 'open';
```

## Типичные ошибки
- проверять только HTTP/UI и не смотреть факт записи в БД
- писать слишком хрупкие DB asserts

## Практика
В `practice.py` есть функции для самостоятельной реализации:
- `critical_defect_exists` - Верни True, если есть хотя бы один critical defect.
- `failed_run_count` - Верни количество failed runs.
- `open_tasks_exist` - Верни True, если есть хотя бы одна open задача.

## Что дальше
Сначала запусти `examples.py`, затем реализуй функции из `practice.py` и сверь вывод с expected.
