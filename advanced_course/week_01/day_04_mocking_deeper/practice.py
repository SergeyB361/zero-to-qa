from unittest.mock import Mock

# День 4 — Практика: mocking deeper

# Задание 1
# Напиши функцию `notify_user(email, mailer)`, которая вызывает:
# mailer.send(email, template="welcome")
# Затем протестируй её через Mock и проверь вызов.


# Задание 2
# Создай Mock-клиент, у которого метод `load()`
# выбрасывает `TimeoutError("service timeout")` через side_effect.
# Проверь, что исключение действительно возникает.


# Задание 3
# Напиши функцию `get_status(api_client)`, которая возвращает
# `api_client.fetch()["status"]`.
# Замокай `fetch()` через return_value и проверь результат.


# Задание 4
# Коротко в комментарии ответь:
# почему patch нужно делать там, где объект используется,
# а не там, где он был изначально объявлен.
