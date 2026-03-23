# API: продвинутый уровень, День 5 — Contract testing

## Зачем это нужно
Contract testing защищает интеграцию между consumer и provider от незаметного drift. Когда форма ответа меняется без согласования, consumer часто ломается не сразу и неочевидно.

## Что важно понять
Contract — это явное ожидание consumer-а к полям, типам, enum и иногда к semantics ответа.

Полезный baseline contract включает:
- required fields
- допустимые типы
- enum values
- backward compatibility для уже используемых полей

## Где contract testing особенно силён
- shared API между командами
- частые изменения схемы
- payload, где consumer зависит от нескольких обязательных полей

## Что он не заменяет
Contract testing не заменяет:
- бизнес-assert
- integration coverage
- end-to-end сценарии

Он отвечает на более узкий вопрос: не сломали ли мы согласованный интерфейс.

## Частые ошибки
- проверять только один удачный payload
- забывать enum и backward compatibility
- считать contract testing полной заменой API suite

## Что запомнить
- contract drift ломает consumer даже при живом endpoint
- required fields и enum — базовый минимум
- contract testing лучше работает как часть общей стратегии
- позитивные и негативные payload нужны оба

## Практика дня
Открой practice.py и сравни ожидаемый контракт с фактическим payload.
