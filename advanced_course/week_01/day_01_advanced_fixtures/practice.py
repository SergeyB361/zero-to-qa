import pytest

# День 1 — Практика: advanced fixtures

# Задание 1
# Напиши fixture `user_profile`, которая возвращает словарь:
# {"email": "qa@example.com", "role": "user"}
# Затем напиши тест, который проверяет email.


# Задание 2
# Напиши fixture `admin_profile`, которая использует `user_profile`
# и меняет роль на `admin`.
# Затем напиши тест на роль.


# Задание 3
# Напиши factory fixture `make_ticket`, которая возвращает функцию.
# Функция должна создавать словарь вида:
# {"title": <title>, "priority": <priority>}
# Используй её в тесте для двух разных тикетов.


# Задание 4
# Напиши yield fixture `resource_log`, которая:
# - до yield добавляет "open"
# - после yield добавляет "close"
# В тесте проверь состояние списка внутри теста.
