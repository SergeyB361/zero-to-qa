# PRIMARY KEY, FOREIGN KEY, связи таблиц

## Зачем это нужно
Без понимания связей невозможно читать схему и строить корректные JOIN. Это база для любой рабочей БД.

## Что нужно понять
- PRIMARY KEY
- FOREIGN KEY
- one-to-many
- ссылочная целостность

## Рабочая логика
1. Определи, из каких таблиц ты читаешь данные.
2. Сузь выборку фильтрами.
3. Только потом добавляй сортировку, группировку или join.
4. Проверяй вывод на маленьком наборе данных.

## Примеры
### Пример 1 - Посмотреть foreign keys таблицы tasks
```sql
PRAGMA foreign_key_list('tasks');
```

### Пример 2 - Посмотреть foreign keys таблицы test_runs
```sql
PRAGMA foreign_key_list('test_runs');
```

### Пример 3 - Связать project -> tasks -> users
```sql
SELECT p.name, t.id, u.name FROM projects AS p JOIN tasks AS t ON p.id = t.project_id JOIN users AS u ON t.assignee_id = u.id ORDER BY p.id, t.id;
```

## Типичные ошибки
- не различать id таблицы и внешний ключ
- строить join по полям без логической связи

## Практика
В `practice.py` есть функции для самостоятельной реализации:
- `tasks_foreign_keys` - Верни количество foreign keys у таблицы tasks.
- `test_runs_foreign_keys` - Верни количество foreign keys у таблицы test_runs.
- `project_task_user_rows` - Верни количество строк в join `projects -> tasks -> users`.

## Что дальше
Сначала запусти `examples.py`, затем реализуй функции из `practice.py` и сверь вывод с expected.
