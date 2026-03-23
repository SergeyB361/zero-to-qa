# API: продвинутый уровень, День 3 — Negative scenarios

## Зачем это нужно
Надёжность API определяется не только успешными ответами, но и качеством обработки ошибок.

Negative scenarios показывают:
- как сервис реагирует на невалидные поля
- корректно ли разделяются 400, 401, 403, 404 и 409
- есть ли стабильный error contract

## Что важно понять
Негативный сценарий — это не просто сломанный запрос. Хороший negative test проверяет:
- код ответа
- понятную ошибку
- отсутствие лишнего side effect
- консистентность error payload

## Типовые негативные зоны
- missing required field
- wrong type
- invalid enum
- conflict state
- unauthorized или forbidden access

## Частые ошибки
- проверять только код ответа без payload
- не отличать validation error от business rule conflict
- не смотреть, что произошло с данными после failed request

## Что запомнить
- negative API tests должны проверять и semantics, и side effects
- коды ошибок должны быть осмысленными
- error payload тоже часть контракта
- конфликт и валидация — не одно и то же

## Практика дня
Открой practice.py и составь негативные сценарии для create и update endpoint.
