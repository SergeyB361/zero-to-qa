# Неделя 2, День 1 — Списки

## Что такое список
Список (`list`) — изменяемая упорядоченная коллекция элементов.

```python
nums = [10, 20, 30]
```

## Базовые операции
- доступ по индексу: `items[0]`
- срезы: `items[1:3]`
- длина: `len(items)`
- добавление: `append()`
- удаление: `remove()`, `pop()`
- сортировка: `sort()`, `sorted()`

## Примеры
```python
items = ["a", "b", "c"]
items.append("d")
print(items)  # ['a', 'b', 'c', 'd']
```

```python
nums = [5, 2, 9, 1]
print(sorted(nums))  # [1, 2, 5, 9]
print(nums)          # исходный список не изменился
nums.sort()
print(nums)          # [1, 2, 5, 9]
```

## List comprehension (введение)
Короткая форма создания списков на основе цикла.

```python
squares = [x * x for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
```

С фильтром:
```python
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]
```

## Частые ошибки
- `items[10]` при коротком списке -> `IndexError`
- путаница `sort()` и `sorted()`
- изменение списка во время итерации

## Практика
Переходи в `practice.py`. Решаем задания по одному.
