# Неделя 2, День 3 — Словари (dict)

## Что такое словарь
Словарь (`dict`) — коллекция пар `ключ: значение`.

```python
user = {"name": "Sergey", "age": 28}
```

## Базовые операции
- доступ: `d[key]`
- безопасный доступ: `d.get(key, default)`
- добавление/изменение: `d[key] = value`
- удаление: `del d[key]`, `d.pop(key)`
- ключи/значения/пары: `keys()`, `values()`, `items()`

## Важно
- ключи должны быть хешируемыми (`str`, `int`, `tuple` и т.д.)
- `d[key]` вызывает `KeyError`, если ключа нет
- `get()` безопаснее для необязательных ключей

## Итерирование
```python
for key, value in user.items():
    print(key, value)
```

## Вложенные словари
```python
profile = {
    "name": "ann",
    "stats": {"tests": 120, "bugs": 14}
}
print(profile["stats"]["tests"])
```

## Практика
Переходи в `practice.py`, решаем задания по одному.
