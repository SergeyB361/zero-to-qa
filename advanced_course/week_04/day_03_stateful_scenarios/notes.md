# API: reliability и integration, День 3 — Stateful scenarios

## Зачем это нужно
- Многие API зависят от состояния и порядка действий.
- Одиночный запрос не показывает корректность жизненного цикла.
- Stateful defects часто возникают на недопустимых переходах.

## Что важно понять
- Нужно проверять allowed transitions и forbidden transitions.
- После ошибки состояние объекта должно оставаться предсказуемым.
- Create -> update -> confirm цепочка часто важнее отдельного GET.

## Частые ошибки
- Проверять только happy path переходы.
- Не проверять состояние после ошибки.
- Считать lifecycle покрытым одним endpoint-тестом.

## Практика дня
Открой practice.py и смоделируй allowed и disallowed transitions.
