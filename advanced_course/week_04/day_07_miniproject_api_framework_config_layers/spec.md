# ТЗ: Мини-проект — API framework with config layers

## Исходный файл
Используй:
- api_framework.py

## Что нужно построить
1. config loader
2. API client layer
3. auth helper
4. diagnostics helper
5. пример stateful или polling сценария

## Обязательные требования
- базовый URL должен приходить через config
- token не должен быть захардкожен в тестах
- failure report должен содержать method, url, status и body
- client и business-level helper должны быть разделены
- должен быть пример одного stateful flow
