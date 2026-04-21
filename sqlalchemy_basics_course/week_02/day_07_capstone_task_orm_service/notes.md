# Capstone — Task ORM Service

## Задача
Собрать маленький service module поверх ORM-моделей `Task` и `TaskComment`.

## Что проверяется
- модели и relationship;
- CRUD и commit-policy;
- repository/service split;
- читаемый итоговый API функций.

## Что считается сильным результатом
- capstone не возвращает hardcoded данные;
- новые комментарии реально сохраняются в БД;
- summary-функция собирает данные из ORM, а не из ручных заглушек.
