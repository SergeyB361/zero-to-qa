# SQLite и PostgreSQL: базовые различия

## Зачем это нужно
Для QA важно понимать, где локальная SQLite удобна, а где в реальном проекте нужна серверная СУБД вроде PostgreSQL.

## Что нужно понять
- embedded vs server DB
- типы и ограничения
- concurrency
- use cases

## Рабочая логика
1. Определи, из каких таблиц ты читаешь данные.
2. Сузь выборку фильтрами.
3. Только потом добавляй сортировку, группировку или join.
4. Проверяй вывод на маленьком наборе данных.

## Примеры
### Пример 1 - SQLite удобна для локальных тестов
```sql
SELECT 'sqlite' AS engine, 'embedded and simple' AS note;
```

### Пример 2 - SQLite version placeholder
```sql
SELECT sqlite_version() AS version;
```

### Пример 3 - PostgreSQL как production reference
```sql
SELECT 'postgres' AS engine, 'server and concurrency' AS note;
```

## Типичные ошибки
- ожидать от SQLite поведения production-СУБД
- думать, что все SQL-диалекты полностью одинаковы

## Практика
В `practice.py` есть функции для самостоятельной реализации:
- `sqlite_strengths` - Верни список из трёх сильных сторон SQLite.
- `postgres_strengths` - Верни список из трёх сильных сторон PostgreSQL.
- `choose_engine` - Для строки case_name верни `sqlite` или `postgres`.

## Что дальше
Сначала запусти `examples.py`, затем реализуй функции из `practice.py` и сверь вывод с expected.
