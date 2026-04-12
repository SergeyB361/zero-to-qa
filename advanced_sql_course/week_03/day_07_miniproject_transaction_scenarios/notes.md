# Мини-проект: transaction scenarios

## Цель
Собрать набор сценариев, где транзакции и ограничения влияют на результат: commit, rollback, invalid insert и audit event.

## Что должно получиться
- `resolve_defect(conn, defect_id, actor_id)`
- `try_invalid_case_insert(conn)`
- `defect_audit_count(conn, defect_id)`
- `main()` с последовательным demo

## Как подходить к проекту
1. Запусти starter-файл и посмотри expected demo flow.
2. Реализуй функции по одной.
3. Проверяй, что SQL остаётся читаемым.
4. В конце оформи нормальный `main()`.
