# SQL debugging workflows

## Зачем это нужно
Когда запрос даёт “не те числа”, нужен не новый random SQL, а дисциплина отладки: сузить выборку, проверить join, проверить промежуточные шаги.

## Ключевые идеи
- isolate step
- count before and after join
- debug with CTE
- compare expected vs actual

## Практический фокус
Хороший workflow: начать с маленького запроса, проверить cardinality, потом наращивать сложность.

## Типичные ошибки
- исправлять запрос вслепую
- не проверять промежуточные количества строк

## Практика
В `practice.py` реализуй функции:
- `count_runs_before_join` - Верни количество строк в test_runs.
- `count_runs_after_join` - Верни количество строк после join test_runs + test_cases.
- `debug_failed_by_release` - Верни пары `build_tag:failed_count` как результат debugged запроса.

## Что дальше
Сначала запусти `examples.py`, затем доведи функции из `practice.py` до expected-результатов.
