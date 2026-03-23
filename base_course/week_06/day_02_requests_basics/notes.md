# Неделя 6, День 2 — requests

## Что такое requests
`requests` — популярная библиотека Python для отправки HTTP-запросов.

## Базовый пример
```python
import requests

response = requests.get("https://reqres.in/api/users/2")
print(response.status_code)
print(response.json())
```

## Что обычно используют
- `requests.get(...)`
- `requests.post(...)`
- `params=` для query-параметров
- `json=` для JSON-тела
- `headers=` для заголовков

## Что важно в объекте response
- `response.status_code`
- `response.json()`
- `response.text`
- `response.headers`

## Практические правила
- если API возвращает JSON, обычно удобно работать через `response.json()`
- не забывай проверять статус-код до глубоких проверок тела
- `json=` предпочтительнее, чем ручная сборка JSON-строки

## Практика дня
Открой `practice.py` и потренируй отправку простых запросов.