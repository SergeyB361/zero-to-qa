# Неделя 3, День 3 — Type hints

## Что такое type hints
Type hints — это подсказки типов в Python.
Они помогают понять, какие данные ожидает функция и что она возвращает.

Type hints:
- не заставляют Python жёстко проверять типы при запуске,
- делают код понятнее,
- помогают редактору и линтерам находить ошибки раньше.

## Базовый пример
```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

Здесь:
- `name: str` — аргумент `name` ожидается как строка
- `-> str` — функция возвращает строку

## Полезные варианты
- `int`, `float`, `str`, `bool`
- `list[str]` — список строк
- `dict[str, int]` — словарь строка -> число
- `tuple[int, int]` — кортеж из двух чисел
- `None` — функция ничего не возвращает

## Optional
Если значение может быть, а может не быть, используют `Optional`.

```python
from typing import Optional

def format_name(name: Optional[str]) -> str:
    if name is None:
        return "Unknown"
    return name.title()
```

## Что важно
- type hints делают код яснее, но сами по себе не заменяют проверки в коде
- особенно полезны в функциях, хелперах и тестовых утилитах

## Практика
Открой `practice.py`, решай по шагам.
