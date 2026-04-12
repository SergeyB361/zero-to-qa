# ТЗ: Мини-проект: transaction scenarios

## Цель
Собрать набор сценариев, где транзакции и ограничения влияют на результат: commit, rollback, invalid insert и audit event.

## Deliverables
- `resolve_defect(conn, defect_id, actor_id)`
- запрос `try_invalid_case_insert`
- `defect_audit_count(conn, defect_id)`
- `transaction_scenarios.sql` с последовательным demo

## MVP-запросы
- `resolve_defect` - Закрывает defect и пишет audit event.
- `try_invalid_case_insert` - Проверяет rollback при invalid owner.
- `defect_audit_count` - Считает audit events по defect.

## Пример допустимого вывода
```text
resolve_defect -> closed
try_invalid_case_insert -> True
defect_audit_count -> 2
```

## Критерии готовности
- SQL-скрипт выполняется без ошибок на подготовленном dataset;
- каждый запрос решает отдельную задачу;
- запросы читаются без магии;
- `transaction_scenarios.sql` показывает рабочий demo flow;
- решение использует темы недели.
