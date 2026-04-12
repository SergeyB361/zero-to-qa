# Итоговая SQL-практика

## Зачем это нужно
Финальный день перед мини-проектом. Здесь важно собрать в одну систему SELECT, DML, JOIN, агрегации, подзапросы и проверки из Python.

## Что нужно понять
- mixed SQL tasks
- чтение данных + изменение + проверка
- подготовка к мини-проекту

## Рабочая логика
1. Определи, из каких таблиц ты читаешь данные.
2. Сузь выборку фильтрами.
3. Только потом добавляй сортировку, группировку или join.
4. Проверяй вывод на маленьком наборе данных.

## Примеры
### Пример 1 - Собрать summary по runs и defects
```sql
SELECT (SELECT COUNT(*) FROM test_runs) AS runs_total, (SELECT COUNT(*) FROM defects WHERE status = 'open') AS open_defects;
```

### Пример 2 - Показать задачи с именем исполнителя и проектом
```sql
SELECT t.id, p.name AS project_name, u.name AS assignee, t.status FROM tasks AS t JOIN projects AS p ON p.id = t.project_id JOIN users AS u ON u.id = t.assignee_id ORDER BY t.id;
```

### Пример 3 - Вывести test_cases без failed runs
```sql
SELECT c.title FROM test_cases AS c WHERE NOT EXISTS (SELECT 1 FROM test_runs AS r WHERE r.case_id = c.id AND r.status = 'failed') ORDER BY c.title;
```

## Типичные ошибки
- бросаться сразу в мини-проект без повторения базовых инструментов

## Практика
В `practice.py` есть функции для самостоятельной реализации:
- `summary_counts` - Верни словарь с общим количеством test_runs и open defects.
- `task_overview_rows` - Верни количество строк в обзоре задач с проектом и исполнителем.
- `stable_case_titles` - Верни test_cases, у которых не было failed run.

## Что дальше
Сначала запусти `examples.py`, затем реализуй функции из `practice.py` и сверь вывод с expected.
