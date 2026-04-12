# EXISTS и NOT EXISTS

## Зачем это нужно
Эти конструкции полезны для вопросов типа “есть ли связанные записи” и “где связанных записей нет”. Это очень частый класс QA-проверок.

## Что нужно понять
- EXISTS
- NOT EXISTS
- коррелированный подзапрос
- проверка наличия зависимых записей

## Рабочая логика
1. Определи, из каких таблиц ты читаешь данные.
2. Сузь выборку фильтрами.
3. Только потом добавляй сортировку, группировку или join.
4. Проверяй вывод на маленьком наборе данных.

## Примеры
### Пример 1 - Test cases, у которых есть failed run
```sql
SELECT c.title FROM test_cases AS c WHERE EXISTS (SELECT 1 FROM test_runs AS r WHERE r.case_id = c.id AND r.status = 'failed') ORDER BY c.title;
```

### Пример 2 - Test cases без failed run
```sql
SELECT c.title FROM test_cases AS c WHERE NOT EXISTS (SELECT 1 FROM test_runs AS r WHERE r.case_id = c.id AND r.status = 'failed') ORDER BY c.title;
```

### Пример 3 - Пользователи, у которых есть open задачи
```sql
SELECT u.name FROM users AS u WHERE EXISTS (SELECT 1 FROM tasks AS t WHERE t.assignee_id = u.id AND t.status = 'open') ORDER BY u.name;
```

## Типичные ошибки
- использовать `IN` там, где логичнее `EXISTS`
- не связывать внутренний и внешний запрос

## Практика
В `practice.py` есть функции для самостоятельной реализации:
- `cases_without_failed_runs` - Верни test_cases, у которых нет failed run.
- `users_with_open_tasks` - Верни имена пользователей, у которых есть open задачи.
- `projects_without_closed_tasks` - Верни проекты, в которых нет задач со status = closed.

## Что дальше
Сначала запусти `examples.py`, затем реализуй функции из `practice.py` и сверь вывод с expected.
