# ТЗ: День 7 - Rich domain model

## Задача

Собери небольшой OOP-мини-проект вокруг task/event-домена.

Нужна не просто коллекция классов, а связная модель, в которой advanced OOP-техники
применены по делу.

## Что нужно реализовать

### Шаг 1 - Value object TaskId

Создай класс `TaskId`:
- хранит строковое значение идентификатора;
- реализует `__str__`;
- реализует `__repr__`;
- реализует `__eq__` и `__hash__`.

Требование:
- два `TaskId` с одинаковым значением должны считаться равными;
- `TaskId` должен корректно работать в `set`.

### Шаг 2 - Reusable descriptors

Реализуй минимум два descriptor-класса:
- `NonEmptyString`
- `ChoiceField`

Требования:
- `NonEmptyString` не принимает пустые строки после `strip()`;
- `ChoiceField` принимает только разрешённые значения.

### Шаг 3 - Callable validator

Реализуй `StatusTransitionValidator`.

Он должен быть вызываемым объектом:

```python
validator("draft", "active")
```

Требование:
- возвращает `True`, если переход допустим;
- возвращает `False`, если переход запрещён.

Минимальные разрешённые переходы:
- `draft -> active`
- `active -> disabled`
- `disabled -> active`

### Шаг 4 - Dynamic payload view

Реализуй `EventPayloadView` через `__getattr__`.

Требование:
- если поле есть в `payload`, оно доступно как атрибут;
- если поля нет, выбрасывается `AttributeError`.

Пример:

```python
payload = EventPayloadView({"actor_id": "user-1", "reason": "manual change"})
payload.actor_id
```

### Шаг 5 - Dataclass model

Создай `TaskRecord` как dataclass.

Требования:
- использует `slots=True`;
- содержит минимум поля:
  - `task_id`
  - `title`
  - `status`
  - `owner`
- имеет читаемый `__repr__` за счёт dataclass.

### Шаг 6 - Mixin behavior

Добавь хотя бы один mixin.

Подходящие варианты:
- `ToDictMixin`
- `DisplayMixin`
- `AuditMixin`

Требование:
- mixin должен добавлять маленькое, но полезное поведение;
- не нужно строить сложную иерархию ради самой иерархии.

## Стартовый файл

Работай в:
- [rich_domain_model.py](C:\Users\serge\zero-to-qa\advanced_course\bonus_advanced_python_oop\day_07_miniproject_rich_domain_model\rich_domain_model.py)

## Ожидаемый demo flow

Файл должен запускаться и показывать примерно такой сценарий:

```text
TaskId equality: True
TaskId set size: 1
Draft title: Fix login
Transition draft -> active: True
Transition draft -> disabled: False
Payload actor_id: user-1
TaskRecord(... )
```

Точный текст может отличаться, но смысл должен совпадать.

## Критерии готовности

Проект можно считать выполненным, если:

1. `TaskId` работает как value object.
2. Descriptor-валидация реально режет неверные значения.
3. `StatusTransitionValidator` вызывается как функция.
4. `EventPayloadView` отдаёт значения из payload через атрибуты.
5. `TaskRecord` оформлен как dataclass со `slots=True`.
6. Есть хотя бы один полезный mixin.
7. `main()` показывает связный demo flow без падений.

## Что не нужно

- не нужно делать production-grade фреймворк;
- не нужно добавлять 10 классов ради количества;
- не нужно использовать все магические методы подряд.

Цель проекта - показать инженерное чувство меры.