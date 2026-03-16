# Неделя 2, День 6 — Практика: множества

# Задание 1
# Создай множество fruits со значениями: "apple", "banana", "apple", "orange".
# Выведи его.

fruits = {"apple", "banana", "apple", "orange"}
print(fruits)


# Задание 2
# Добавь в fruits элемент "mango".
# Затем удали "banana" без ошибки, если элемента нет.
# Выведи результат.

fruits.add("mango")
fruits.discard("banana")

print(fruits)


# Задание 3
# Даны множества:
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# Выведи:
# - объединение
# - пересечение
# - разность a и b
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b) # or
print(a & b) # and
print(a - b) # or


# Задание 4
# Дан список: ["qa", "python", "qa", "api", "python"]
# Убери дубликаты через set и выведи результат.

items = ["qa", "python", "qa", "api", "python"]
items_no_double = set(items)
print(items_no_double)