# ТЗ: Мини-проект — DB Checks Toolkit

## Цель
Собрать маленький toolkit для Postgres-проверок из Python: existence checks, counts, scalar values и status distribution.

## Deliverables
- функция `row_exists(conn, query)`
- функция `count_rows(conn, query)`
- функция `get_scalar(conn, query)`
- функция `status_distribution(conn, table_name, column_name)`
- демо `main()` в `db_checks_toolkit.py`

## Критерии готовности
- файл запускается без ошибок;
- каждая функция решает одну понятную задачу;
- `main()` показывает рабочий demo flow против `zero_to_qa`.
