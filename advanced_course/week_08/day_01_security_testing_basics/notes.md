# Senior QA Engineering, День 1 — Security testing basics

## Зачем это нужно
- QA должен понимать базовые security risk, даже если не является security engineer.
- Многие критичные дефекты связаны с auth, access control и утечкой данных.
- Security mindset усиливает обычное функциональное тестирование.

## Что важно понять
- Базовый набор: auth, authorization, input validation, secret exposure.
- Нужно мыслить сценариями abuse, а не только happy path.
- Security testing начинается с простых проверок, а не с экзотики.

## Частые ошибки
- Считать security задачей только отдельной команды.
- Проверять только логин и забывать про права доступа.
- Логировать чувствительные данные в тестах.

## Практика дня
Открой practice.py и перечисли базовые security checks для API и UI.
