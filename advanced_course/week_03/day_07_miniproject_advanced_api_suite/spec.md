# ТЗ: Мини-проект — advanced API suite

## Исходный файл
Используй:
- orders_api.py

## Что должно быть в suite
1. auth tests
2. negative payload tests
3. contract и schema checks
4. retry и idempotency сценарии
5. mock-based tests для внешнего provider

## Обязательные требования
- минимум 10 тестов
- минимум один параметризованный negative test
- минимум один auth scenario с invalid token
- минимум один contract check
- минимум один mock scenario
- минимум один сценарий с повторным вызовом и анализом idempotency

## Рекомендуемая структура
- test_auth.py
- test_negative.py
- test_contracts.py
- test_idempotency.py
- test_external_provider.py
