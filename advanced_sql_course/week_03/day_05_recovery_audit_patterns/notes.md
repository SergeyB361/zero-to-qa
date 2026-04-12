# Recovery и audit patterns

## Зачем это нужно
В реальных системах важно не только менять данные, но и понимать, как восстановить историю и кто что сделал.

## Ключевые идеи
- audit trail
- soft delete
- recovery-friendly schema
- who/when changed data

## Практический фокус
Даже простой audit_log уже помогает разбирать инциденты и воспроизводить цепочку событий.

## Типичные ошибки
- терять историю после update/delete
- не хранить actor и timestamp

## Практика
В `practice.sql` напиши запросы:
- `audit_events_for_defects` - Верни пары `entity_id:action` для defect events.
- `open_defects_with_owner` - Верни пары `defect:owner` для open defects.
- `soft_close_summary` - Верни количество closed defects.

## Что дальше
Сначала выполни `examples.sql`, затем доведи запросы из `practice.sql` до expected-результатов.
