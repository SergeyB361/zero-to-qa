# ТЗ: Мини-проект: маленькая схема данных

## Цель
Создать небольшую схему в SQLite, наполнить её тестовыми данными и выполнить несколько проверочных запросов.

## Deliverables
- функция `create_schema(conn)`
- функция `seed_data(conn)`
- функция `list_tables(conn)`
- функция `query_task_overview(conn)`
- демо `main()`

## Функции MVP
- `create_schema` - Создай маленькую схему из users, projects и tasks.
- `seed_data` - Добавь demo-данные в новую схему.
- `list_tables` - Верни список таблиц новой схемы.
- `query_task_overview` - Верни обзор задач с join по новой схеме.

## Пример допустимого вывода
```text
Tables: ['projects', 'tasks', 'users']
Task overview rows: 3
```

## Критерии готовности
- файл запускается без ошибок;
- каждая функция решает одну понятную задачу;
- запросы читаются;
- `main()` показывает рабочий demo flow.
