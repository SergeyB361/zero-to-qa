# ТЗ: Мини-проект: маленькая схема данных

## Цель
Создать небольшую схему в SQLite, наполнить её тестовыми данными и выполнить несколько проверочных запросов.

## Deliverables
- запрос `create_schema`
- запрос `seed_data`
- запрос `list_tables`
- запрос `query_task_overview`
- демо `small_schema.sql`

## MVP-запросы
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
- SQL-скрипт выполняется без ошибок на подготовленном dataset;
- каждый запрос решает одну понятную задачу;
- запросы читаются;
- `small_schema.sql` показывает рабочий demo flow.
