# Неделя 2, День 6 — Дополнительная практика: итерация по множествам

# Задание 1
# Дан set:
# colors = {"red", "green", "blue"}
# Выведи каждый цвет отдельно в цикле.

colors = {"red", "green", "blue"}
for color in colors:
    print(color)


# Задание 2
# Дан set:
# numbers = {3, 7, 2, 9}
# Выведи сумму всех элементов без sum(), только через цикл.

numbers = {3, 7, 2, 9}
sum_number = 0
for number in numbers:
    sum_number +=number
    
print(sum_number)

# Задание 3
# Дан set:
# words = {"python", "qa", "automation", "api"}
# Выведи только слова, длина которых больше 3.

words = {"python", "qa", "automation", "api"}

more_3 = {word for word in words if len(word) > 3}
print(more_3)

# Задание 4
# Дан set:
# skills = {"python", "sql", "pytest", "git"}
# Посчитай, сколько элементов в множестве, не используя len().
skills = {"python", "sql", "pytest", "git"}
#print(len(skills))
i = 0
for slill in skills:
    i += 1

print(i)



# Задание 5
# Дан set:
# values = {2, 4, 6, 8, 10}
# Выведи только те элементы, которые больше 5.

values = {2, 4, 6, 8, 10}
more_5 = {value for value in values if value > 5}
print(more_5)


# Задание 6
# Дан set:
# names = {"anna", "ivan", "olga", "sergey"}
# Создай новый список, в который добавь имена из множества в верхнем регистре через цикл.
names = {"anna", "ivan", "olga", "sergey"}
u = []
for name in names:
    x = name.upper()
    u.append(x)

print(u)


# Задание 7
# Дан set:
# nums = {1, 2, 3, 4, 5}
# Найди произведение всех чисел через цикл.

nums = {1, 2, 3, 4, 5}
multi = 1

for num in nums:
    multi = num * multi

print(multi)


# Задание 8
# Дан set:
# letters = {"a", "b", "c", "d"}
# Собери строку из всех букв через цикл и не используй join().

letters = {"a", "b", "c", "d"}
item = ""

for letter in letters:
    item += str(letter)

print(item)


# Задание 9
# Дан set:
# items = {"apple", "banana", "pear", "plum"}
# Найди самое длинное слово через цикл.

items = {"apple", "banana", "pear", "plum"}
max_item = ""

for item in items:
    if len(item) > len(max_item):
        max_item = item
    
print(max_item)



# Задание 10
# Дан set:
# scores = {78, 91, 66, 100, 84}
# Посчитай, сколько значений не меньше 80.

scores = {78, 91, 66, 100, 84}
more_80 = {score for score in scores if score > 80}
print(len(more_80))

