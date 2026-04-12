# ТЗ: Финальный мини-проект: DB Checks Toolkit

## Цель
Собрать маленький toolkit для SQL-проверок из Python: existence checks, counts, scalar values и простые QA-assertions.

## Deliverables
- функция `row_exists(conn, query)`
- функция `count_rows(conn, query)`
- функция `get_scalar(conn, query)`
- функция `status_distribution(conn, table_name, column_name)`
- демо `main()`

## Функции MVP
- `row_exists` - Верни True, если запрос возвращает хотя бы одну строку.
- `count_rows` - Верни количество строк по запросу.
- `get_scalar` - Верни скалярное значение из запроса.
- `status_distribution` - Верни словарь status -> count по таблице и колонке.

## Пример допустимого вывода
```text
Critical defect exists: True
Open tasks count: 3
Run status distribution: {'failed': 2, 'passed': 3, 'skipped': 1}
```

## Критерии готовности
- файл запускается без ошибок;
- каждая функция решает одну понятную задачу;
- запросы читаются;
- `main()` показывает рабочий demo flow.
