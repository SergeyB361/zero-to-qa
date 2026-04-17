# Практика на consistency

## Зачем нужен этот день
На этой неделе ты увидел ACID, isolation, locks, deadlocks, constraints и MVCC. Здесь задача — собрать их в одну рабочую модель согласованности данных в Postgres.

## Что считается хорошим решением
Хорошее решение различает blocking и deadlock, понимает роль constraints и умеет раскладывать сценарий на session A / session B.
