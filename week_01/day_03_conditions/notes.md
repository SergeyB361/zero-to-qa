# Неделя 1, День 3 — Условия

> Основано на: «Python Crash Course» — Eric Matthes, «Изучаем Python» — Марк Лутц

---

## 1. Синтаксис if / elif / else

Условная конструкция управляет ветвлением выполнения программы.
Python использует **отступы** (4 пробела) вместо фигурных скобок — это часть синтаксиса, не стиль.

```python
score = 85

if score >= 90:
    print("Отлично")
elif score >= 70:
    print("Хорошо")
elif score >= 50:
    print("Удовлетворительно")
else:
    print("Не сдал")
```

**Правила:**
- `if` — обязателен, один
- `elif` — опционален, любое количество
- `else` — опционален, один, всегда последний
- Двоеточие `:` обязательно после каждого условия
- Тело блока — минимум одна инструкция с отступом

### Как if работает механически

1. Вычисляется выражение после `if` — получается объект
2. Объект неявно приводится к `bool` через `bool()`
3. Если результат `True` — выполняется тело блока, остальные ветки пропускаются
4. Если `False` — переходит к следующему `elif` или `else`

```python
if score >= 90:
    print("Отлично")
```

Это буквально:
```python
if bool(score >= 90) == True:
    print("Отлично")
```

Поэтому в условии работает любой объект, не только явный `bool`:

```python
if "hello":      # bool("hello") → True
if 0:            # bool(0) → False
if [1, 2]:       # bool([1, 2]) → True
if None:         # bool(None) → False
```

**Важно:** `elif` проверяется только если все предыдущие условия были `False`.
Как только одна ветка сработала — остальные не проверяются вообще:

```python
x = 10
if x > 5:
    print("больше 5")    # ← выполнится это
elif x > 3:
    print("больше 3")    # ← сюда код НЕ дойдёт, хотя условие тоже True
```

---

## 2. Операторы сравнения

```python
x == y    # равно
x != y    # не равно
x > y     # больше
x < y     # меньше
x >= y    # больше или равно
x <= y    # меньше или равно
```

Возвращают `bool`: `True` или `False`.

```python
print(10 > 5)     # True
print(10 == 10)   # True
print(10 != 5)    # True
print("a" < "b")  # True — строки сравниваются лексикографически
```

---

## 3. Логические операторы: and, or, not

Объединяют несколько условий в одно выражение.

```python
age = 25
has_experience = True

# and — оба условия должны быть True
if age >= 18 and has_experience:
    print("Подходит")

# or — достаточно одного True
if age < 18 or age > 65:
    print("Не в рабочем возрасте")

# not — инвертирует значение
if not has_experience:
    print("Опыта нет")
```

### Приоритет операторов

```python
# not → and → or (от высшего к низшему)
True or False and False    # True  (and выполняется первым)
(True or False) and False  # False (скобки меняют порядок)
```

Когда неочевидно — используй скобки. Код читается людьми.

### Короткое замыкание (short-circuit evaluation)

Python прекращает вычисление как только результат известен:

```python
# and: если первое False — второе не вычисляется
False and some_function()   # some_function не вызовется

# or: если первое True — второе не вычисляется
True or some_function()     # some_function не вызовется
```

Это важно при работе с потенциально опасными операциями:
```python
# Безопасная проверка деления
if divisor != 0 and value / divisor > 1:
    print("Больше единицы")
```

---

## 4. Проверка принадлежности: in и not in

```python
status = "active"
valid_statuses = ["active", "pending", "blocked"]

if status in valid_statuses:
    print("Статус корректный")

if "admin" not in status:
    print("Не администратор")
```

Работает для строк, списков, кортежей, множеств, словарей (по ключам).

```python
# Для строк — поиск подстроки
if "error" in log_message.lower():
    print("Найдена ошибка в логе")
```

---

## 5. Тернарный оператор (conditional expression)

Однострочная форма if/else. Используется когда нужно выбрать одно из двух значений.

```python
# Синтаксис: значение_если_true if условие else значение_если_false
age = 20
status = "совершеннолетний" if age >= 18 else "несовершеннолетний"
print(status)    # совершеннолетний

# В f-строке
score = 95
print(f"Результат: {'PASS' if score >= 60 else 'FAIL'}")
```

Не злоупотребляй: если условие сложное — обычный if читается лучше.

---

## 6. Истинность в условиях (Truthiness)

Python не требует явного `== True`. Любой объект можно использовать как условие.

```python
name = "Sergey"
items = [1, 2, 3]
count = 0

if name:           # True — непустая строка
    print("Имя задано")

if items:          # True — непустой список
    print("Список не пустой")

if not count:      # True — 0 это falsy
    print("Счётчик равен нулю")
```

**Falsy значения** (всё остальное — truthy):
```python
False, None, 0, 0.0, "", [], {}, set()
```

В реальном коде `if items:` предпочтительнее `if len(items) > 0:` — короче и идиоматичнее.

---

## 7. Вложенные условия

```python
role = "tester"
level = "senior"

if role == "tester":
    if level == "senior":
        print("Senior QA")
    elif level == "middle":
        print("Middle QA")
    else:
        print("Junior QA")
else:
    print("Не тестировщик")
```

Глубокая вложенность ухудшает читаемость. Если видишь 3+ уровня — стоит рефакторить.
Часто можно заменить вложенное условие на `and`:

```python
# Вложенное (хуже)
if role == "tester":
    if level == "senior":
        print("Senior QA")

# Плоское (лучше)
if role == "tester" and level == "senior":
    print("Senior QA")
```

---

## 8. Паттерн match/case (Python 3.10+)

Структурное сопоставление с образцом — альтернатива длинным if/elif цепочкам.

```python
http_status = 404

match http_status:
    case 200:
        print("OK")
    case 400:
        print("Bad Request")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print(f"Неизвестный статус: {http_status}")
```

`case _` — аналог `else`, совпадает с чем угодно.

Для QA особенно полезен при обработке HTTP-статусов и кодов ошибок.

---

## Итог

```
if / elif / else  → ветвление выполнения
==, !=, >, <      → операторы сравнения, возвращают bool
and, or, not      → логические операторы
in / not in       → проверка принадлежности
x if cond else y  → тернарный оператор
match/case        → структурное сопоставление (Python 3.10+)
```

---

## Практика → [practice.py](practice.py)
