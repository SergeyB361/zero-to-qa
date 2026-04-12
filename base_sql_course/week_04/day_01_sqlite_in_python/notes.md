# SQLite в Python

## Зачем это нужно
Это мост между SQL и обычным Python-кодом. Именно так SQL часто используется в автотестах, утилитах и локальных проверках.

## Что нужно понять
- sqlite3.connect
- cursor/execute
- fetchall/fetchone
- row_factory

## Рабочая логика
1. Определи, из каких таблиц ты читаешь данные.
2. Сузь выборку фильтрами.
3. Только потом добавляй сортировку, группировку или join.
4. Проверяй вывод на маленьком наборе данных.

## Примеры
### Пример 1 - Получить список пользователей
```sql
SELECT id, name FROM users ORDER BY id;
```

### Пример 2 - Получить одно скалярное значение
```sql
SELECT COUNT(*) AS run_count FROM test_runs;
```

### Пример 3 - Прочитать только failed runs
```sql
SELECT id, status FROM test_runs WHERE status = 'failed' ORDER BY id;
```

## Типичные ошибки
- не закрывать connection
- не коммитить изменения
- тащить всю постобработку в Python вместо SQL

## Практика
В `practice.py` есть функции для самостоятельной реализации:
- `list_user_names` - Верни список имён пользователей через sqlite3.
- `count_test_runs` - Верни количество test_runs.
- `failed_run_ids` - Верни id failed test_runs.

## Что дальше
Сначала запусти `examples.py`, затем реализуй функции из `practice.py` и сверь вывод с expected.
