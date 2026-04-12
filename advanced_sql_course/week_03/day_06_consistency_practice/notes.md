# Практика на consistency

## Зачем это нужно
Этот день собирает вместе транзакции, ограничения и audit-паттерны: не просто запрос написать, а сохранить согласованность данных.

## Ключевые идеи
- transaction + constraint + audit
- negative testing on DB layer
- consistency checks

## Практический фокус
Думай не только о happy path, но и о том, что должно не сработать.

## Типичные ошибки
- не проверять состояние БД после rollback или failed insert

## Практика
В `practice.py` реализуй функции:
- `resolve_defect_in_transaction` - Закрой defect id = 1 и добавь audit event в одной транзакции.
- `rollback_on_invalid_owner` - Верни True, если invalid insert не меняет количество test_cases.
- `audit_count_after_resolution` - Верни количество audit events для defect после успешного закрытия.

## Что дальше
Сначала запусти `examples.py`, затем доведи функции из `practice.py` до expected-результатов.
