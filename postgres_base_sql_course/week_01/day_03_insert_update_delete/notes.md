# INSERT, UPDATE, DELETE

## Когда это нужно
SQL нужен не только для чтения. В реальной работе очень часто приходится:
- подготовить тестовые данные перед сценарием;
- изменить состояние записи;
- убрать временные данные после проверки.

Для этого нужны `INSERT`, `UPDATE` и `DELETE`.

## Что делает каждая команда
- `INSERT` добавляет новые строки;
- `UPDATE` меняет существующие строки;
- `DELETE` удаляет строки.

Это уже изменение состояния базы, а не просто чтение.

## INSERT
Базовый синтаксис:
```sql
INSERT INTO table_name (col1, col2)
VALUES (value1, value2);
```

В Postgres полезно сразу привыкать не забивать identity-id руками без причины. Если колонка создаётся как `GENERATED ... AS IDENTITY`, обычно ты вставляешь только бизнес-данные, а id генерируется автоматически.

Пример:
```sql
INSERT INTO test_cases (title, area, priority)
VALUES ('Reset password', 'auth', 'medium');
```

### Postgres-особенность: RETURNING
Postgres умеет сразу вернуть вставленную или изменённую строку:
```sql
INSERT INTO test_cases (title, area, priority)
VALUES ('Reset password', 'auth', 'medium')
RETURNING id, title;
```

Это очень полезно и в реальной разработке, и в тестах.

## UPDATE
Базовый синтаксис:
```sql
UPDATE table_name
SET col1 = value1
WHERE condition;
```

Главное правило: `UPDATE` почти всегда должен иметь `WHERE`.
Без `WHERE` изменятся все строки таблицы.

Пример:
```sql
UPDATE tasks
SET status = 'closed', closed_at = NOW()
WHERE id = 1;
```

## DELETE
Базовый синтаксис:
```sql
DELETE FROM table_name
WHERE condition;
```

Тот же принцип: `DELETE` без `WHERE` удалит все строки таблицы.

Пример:
```sql
DELETE FROM defects
WHERE id = 2;
```

## Безопасный workflow
Нормальная привычка для изменяющих запросов:
1. сначала `SELECT` и убедиться, что ты нашёл нужные строки;
2. потом `INSERT`, `UPDATE` или `DELETE`;
3. потом проверочный `SELECT` или `RETURNING`.

## Почему для обучения полезны транзакции
Когда ты учишься, удобно заворачивать примеры в `BEGIN` / `ROLLBACK`, чтобы не портить dataset навсегда.

Это позволяет:
- попробовать изменение;
- увидеть результат;
- откатить его и вернуть исходное состояние.

## Частые ошибки
- писать `UPDATE` без `WHERE`;
- писать `DELETE` без `WHERE`;
- забивать id вручную, хотя Postgres может сгенерировать его сам;
- не проверять результат после изменения;
- менять данные и забывать вернуть dataset в исходное состояние.

## Что нужно понимать перед практикой
Перед `practice.sql` ты должен понимать:
1. базовый синтаксис `INSERT`, `UPDATE`, `DELETE`;
2. зачем нужен `WHERE` для `UPDATE` и `DELETE`;
3. почему `RETURNING` — сильный инструмент именно в Postgres.
