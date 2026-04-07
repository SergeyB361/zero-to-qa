# ТЗ: Система пользователей

Реализуй в `users_system.py`:

## 1. Класс `User`
- поля: `username`, `email`
- приватный атрибут `_active` со значением `True` по умолчанию
- метод `deactivate()`, который переводит пользователя в неактивное состояние
- property `is_active` для чтения статуса
- метод `describe()`, который возвращает строку:
  - `"User(username=<username>, active=<True/False>)"`

## 2. Класс `Admin(User)`
- наследуется от `User`
- дополнительное поле `permissions` (список строк)
- использует `super().__init__`
- метод `has_permission(permission)`, который возвращает `True` или `False`
- переопредели `describe()`, чтобы возвращалась строка:
  - `"Admin(username=<username>, permissions=<count>, active=<True/False>)"`

## 3. Функция `print_access_report(user)`
- принимает объект `User` или `Admin`
- печатает результат `describe()`
- если передан `Admin`, дополнительно печатает:
  - `"Can delete: <True/False>"`
  - проверять permission `"delete"`

## 4. Точка входа
- создай обычного пользователя и одного администратора
- выведи отчёт для обоих
- деактивируй обычного пользователя и снова выведи отчёт

## Ожидаемый demo flow
Пример допустимого результата:

```text
=== Access report ===
User(username=anna, active=True)
Admin(username=root, permissions=3, active=True)
Can delete: True

=== After deactivation ===
User(username=anna, active=False)
```

Точные имена пользователей могут отличаться, но структура вывода должна быть такой же по смыслу.

## Критерии готовности
Проект можно считать завершённым, если:
- `users_system.py` запускается без ошибок;
- `User` и `Admin` реализованы через ООП, а не через словари;
- `Admin` реально наследуется от `User`;
- `print_access_report()` работает и для `User`, и для `Admin`;
- деактивация пользователя меняет итоговый вывод;
- код читается без лишнего дублирования.

## Подсказка по проверке
Основная рабочая заготовка для студента: `users_system.py`.

Если нужно свериться после самостоятельной попытки, эталонная реализация лежит в:
- `solution_users_system.py`
