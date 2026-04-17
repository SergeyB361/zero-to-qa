# ТЗ: Мини-проект — transaction scenarios

## Цель
Собрать набор демонстрационных Postgres-сценариев по isolation, blocking и deadlocks.

## Deliverables
- блок `isolation_case`
- блок `blocking_case`
- блок `deadlock_case`
- блок `inspection_queries`
- один SQL-файл `transaction_scenarios.sql`

## Обязательные требования
- используй dataset из `postgres_lab`;
- для blocking/deadlock сценариев явно раздели шаги по session A / session B;
- добавь cleanup-блоки;
- добавь минимум один inspection-запрос к `pg_stat_activity` или `pg_locks`.
