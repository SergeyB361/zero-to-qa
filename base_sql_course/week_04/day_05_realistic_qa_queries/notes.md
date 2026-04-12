# Реалистичные SQL-запросы для QA

## Зачем это нужно
Этот день про реальные вопросы: какие тесты падают, где открытые критичные дефекты, какие сценарии выглядят flaky.

## Что нужно понять
- QA reporting
- поиск проблемных зон
- агрегации + фильтрация + join

## Рабочая логика
1. Определи, из каких таблиц ты читаешь данные.
2. Сузь выборку фильтрами.
3. Только потом добавляй сортировку, группировку или join.
4. Проверяй вывод на маленьком наборе данных.

## Примеры
### Пример 1 - Test cases, у которых были и failed, и passed run
```sql
SELECT c.title FROM test_cases AS c WHERE EXISTS (SELECT 1 FROM test_runs AS r WHERE r.case_id = c.id AND r.status = 'failed') AND EXISTS (SELECT 1 FROM test_runs AS r WHERE r.case_id = c.id AND r.status = 'passed') ORDER BY c.title;
```

### Пример 2 - Открытые дефекты по severity
```sql
SELECT severity, COUNT(*) AS defect_count FROM defects WHERE status = 'open' GROUP BY severity ORDER BY severity;
```

### Пример 3 - Средняя длительность runs по area
```sql
SELECT c.area, AVG(r.duration_sec) AS avg_duration FROM test_cases AS c JOIN test_runs AS r ON c.id = r.case_id GROUP BY c.area ORDER BY avg_duration DESC;
```

## Типичные ошибки
- делать красивый SQL, который не отвечает на инженерный вопрос
- не проверять edge cases вроде skipped или нулевой длительности

## Практика
В `practice.py` есть функции для самостоятельной реализации:
- `flaky_case_titles` - Верни названия test_cases, у которых есть и passed, и failed runs.
- `open_defects_by_severity` - Верни словарь severity -> count только для open defects.
- `avg_duration_by_area` - Верни пары `area:avg_duration`.

## Что дальше
Сначала запусти `examples.py`, затем реализуй функции из `practice.py` и сверь вывод с expected.
