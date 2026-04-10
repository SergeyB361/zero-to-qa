# ТЗ: Route Finder

Реализуй проект в `route_finder.py`.

## Что должно быть в MVP
1. `reachable(graph, start, target)`
2. `shortest_distance(graph, start, target)`
3. `restore_path(graph, start, target)`
4. `main()` с демонстрацией

## Условия
- граф считается невзвешенным;
- для поиска кратчайшего расстояния используй BFS;
- маршрут можно восстанавливать через `parent` map.

## Пример допустимого графа
```python
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": ["F"],
    "E": ["F"],
    "F": []
}
```

## Пример допустимого вывода
```text
Reachable A -> F: True
Shortest distance A -> F: 3
Path A -> F: ['A', 'B', 'D', 'F']
```

## Критерии готовности
- файл запускается без ошибок;
- для расстояния используется BFS;
- путь восстанавливается через parents;
- вывод читается без открытия кода.
