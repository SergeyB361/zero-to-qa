# Неделя 4, День 2 — Методы

## Что такое методы
Методы — это функции внутри класса. Они описывают поведение объекта или самого класса.

## Виды методов
- обычный метод: работает с объектом через `self`
- `@classmethod`: работает с классом через `cls`
- `@staticmethod`: логически относится к классу, но не использует `self` и `cls`

## Пример
```python
class User:
    total = 0

    def __init__(self, name):
        self.name = name
        User.total += 1

    def greet(self):
        return f"Hello, {self.name}"

    @classmethod
    def count(cls):
        return cls.total

    @staticmethod
    def is_valid_name(name):
        return len(name) >= 2
```

## Когда что использовать
- обычный метод: читает или меняет состояние объекта
- `@classmethod`: фабрики, счётчики, работа с данными класса
- `@staticmethod`: утилиты и проверки

## Практика
Открой `practice.py` и попробуй все три вида методов.
