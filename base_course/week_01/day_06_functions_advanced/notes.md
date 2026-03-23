# Неделя 1, День 6 — Функции: продвинуто

## Что изучаем сегодня
- параметры по умолчанию
- `*args` (произвольное число позиционных аргументов)
- `**kwargs` (произвольное число именованных аргументов)
- `lambda` (короткие анонимные функции)

## 1) Параметры по умолчанию
```python
def greet(name, role="QA"):
    return f"Привет, {name}! Роль: {role}"
```

Если аргумент не передан, берется значение по умолчанию.

## 2) *args
`*args` собирает позиционные аргументы в кортеж.

```python
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3))      # 6
print(total(10, 20, 30, 5)) # 65
```

## 3) **kwargs
`**kwargs` собирает именованные аргументы в словарь.

```python
def build_user(**data):
    return data

print(build_user(name="Sergey", role="tester"))
# {'name': 'Sergey', 'role': 'tester'}
```

## 4) lambda
`lambda` — короткая функция-выражение.

```python
square = lambda x: x * x
print(square(5))  # 25
```

Часто используется в `sorted`, `map`, `filter`.

```python
users = [
    {"name": "Ann", "age": 30},
    {"name": "Bob", "age": 25}
]

users_sorted = sorted(users, key=lambda u: u["age"])
```

## Практика
Переходи в `practice.py`. Решаем задания по одному и проверяем.
