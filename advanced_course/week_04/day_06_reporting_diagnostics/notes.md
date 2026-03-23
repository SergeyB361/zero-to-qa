# API: reliability и integration, День 6 — Reporting и diagnostics

## Зачем это нужно
Ценность автотеста определяется не только тем, что он падает, но и тем, насколько быстро по нему можно понять причину. Хорошая диагностика сокращает время разбора инцидента.

## Что важно понять
Для failed API test полезно сохранять:
- request method и URL
- request payload
- response status
- response body
- correlation id или trace id
- ключевые business identifiers

## Где ломаются suites
- в отчёте есть только assert failed
- нет ответа сервера
- не видно, какой тестовый объект использовался
- секреты и лишний шум попадают в лог целиком

## Практический баланс
Нужны:
- достаточно данных для расследования
- без утечки секретов
- без giant logs на каждый happy test

## Что запомнить
- good diagnostics ускоряет расследование в разы
- status, body и identifiers — базовый минимум
- correlation id сильно помогает на distributed systems
- redact secrets before logging

## Практика дня
Открой practice.py и собери диагностический набор полей для failed API test.
