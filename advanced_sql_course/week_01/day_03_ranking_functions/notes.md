# ROW_NUMBER, RANK, DENSE_RANK

## Зачем это нужно
Ранжирование нужно, когда надо находить top-N, лидеров и позиции внутри группы.

## Ключевые идеи
- ROW_NUMBER
- RANK
- DENSE_RANK
- ранжирование внутри группы

## Практический фокус
Это полезно для leaderboard-отчётов, top slow endpoints и приоритизации проблемных сценариев.

## Типичные ошибки
- не различать `RANK` и `DENSE_RANK`
- забывать PARTITION BY, когда рейтинг нужен внутри группы

## Практика
В `practice.py` реализуй функции:
- `rank_cases_by_failures` - Верни пары `title:rank` по числу failed runs.
- `row_number_runs_per_engineer` - Верни пары `run_id:row_number` внутри engineer_id по времени.
- `dense_rank_endpoints_by_latency` - Верни пары `endpoint:rank` по средней latency.

## Что дальше
Сначала запусти `examples.py`, затем доведи функции из `practice.py` до expected-результатов.
