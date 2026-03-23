# API: reliability и integration, День 5 — API test architecture

## Зачем это нужно
Когда API suite растёт, тесты нельзя держать набором raw requests вперемешку с assert и fixture логикой. Нужна архитектура слоёв.

## Что важно понять
Базовое разделение обычно выглядит так:
- client или transport layer
- data builders и fixtures
- assertion helpers
- tests

Это помогает:
- не дублировать запросы
- отделять transport от business asserts
- переиспользовать setup и helpers

## Хорошая архитектура
Хороший признак: тест сверху вниз читается как сценарий, а детали HTTP запроса спрятаны в client layer.

Плохой признак:
- URL и payload размазаны по тестам
- assert и HTTP детали смешаны в одном месте
- один супер-класс делает всё

## Что запомнить
- test code тоже требует архитектуры
- transport, data и asserts должны быть разделены
- клиент должен скрывать механику, но не прятать важный domain signal
- архитектура должна уменьшать стоимость изменений, а не добавлять ceremony

## Практика дня
Открой practice.py и разложи API framework на слои.
