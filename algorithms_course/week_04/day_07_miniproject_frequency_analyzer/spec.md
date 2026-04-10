# ТЗ: Frequency Analyzer

Реализуй проект в `frequency_analyzer.py`.

## Что должно быть в MVP
1. `build_frequency_map(items)`
2. `count_unique(items)`
3. `most_frequent(items)`
4. `items_with_frequency_one(items)`
5. `main()` с понятной демонстрацией

## Demo flow
Используй список вроде:

```python
["api", "ui", "api", "db", "ui", "api", "perf"]
```

И покажи:
- frequency map;
- число уникальных значений;
- самый частый элемент;
- список значений, которые встретились один раз.

## Пример допустимого вывода
```text
Frequency map: {'api': 3, 'ui': 2, 'db': 1, 'perf': 1}
Unique count: 4
Most frequent: api
Frequency one: ['db', 'perf']
```

## Критерии готовности
- проект запускается без ошибок;
- логика разбита на функции;
- не используется лишний перебор там, где уже построена frequency map;
- вывод читается без открытия кода.
