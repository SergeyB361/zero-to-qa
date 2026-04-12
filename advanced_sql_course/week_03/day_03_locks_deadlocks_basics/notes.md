# Locks и deadlocks: база

## Зачем это нужно
Когда несколько процессов хотят менять одни и те же данные, нужны блокировки. Иначе согласованность быстро ломается.

## Ключевые идеи
- lock
- write lock
- deadlock as concept
- SQLite locking limitations

## Практический фокус
На SQLite удобно показать write lock и ошибку `database is locked`. Этого достаточно, чтобы понять идею contention.

## Типичные ошибки
- ожидать, что SQLite покажет server-level deadlock один в один
- не закрывать транзакции и держать lock слишком долго

## Практика
В `practice.sql` реализуй функции:
- `lock_error_happens` - Верни True, если второй writer ловит `database is locked`.
- `sqlite_deadlock_note` - Верни строку о том, что deadlocks чаще обсуждаются в server DB.
- `released_lock_allows_write` - Верни True, если после commit второй writer может обновить строку.

## Что дальше
Сначала запусти `examples.sql`, затем доведи функции из `practice.sql` до expected-результатов.
