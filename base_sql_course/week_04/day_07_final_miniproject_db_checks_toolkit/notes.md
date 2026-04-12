# Финальный мини-проект: DB Checks Toolkit

## Что это за проект
Собрать маленький toolkit для SQL-проверок из Python: existence checks, counts, scalar values и простые QA-assertions.

## Что должно получиться
- функция `row_exists(conn, query)`
- функция `count_rows(conn, query)`
- функция `get_scalar(conn, query)`
- функция `status_distribution(conn, table_name, column_name)`
- демо `main()`

## Как идти по проекту
1. Запусти starter-файл и посмотри expected demo flow.
2. Реализуй функции по одной.
3. После каждой функции сверь вывод `main()`.
4. В конце почисти код и названия.
