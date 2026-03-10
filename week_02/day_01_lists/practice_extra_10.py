# Неделя 2, День 1 — Дополнительные задания (Списки)
# Формат: от простого к сложному. Решай по порядку.

# Задача 1
# Дан список nums = [5, 8, 2, 9, 1]
# Выведи:
# 1) первый элемент
# 2) последний элемент
# 3) длину списка
nums = [5, 8, 2, 9, 1]
print(nums[0])
print(nums[-1])
print(len(nums))

# Задача 2
# Дан список nums = [10, 20, 30]
# 1) Добавь в конец 40
# 2) Добавь в начало 5 (без готовых библиотек)
# 3) Выведи итоговый список
nums = [10, 20, 30]
nums.append(40)
nums.insert(0, 5)
print(nums)

# Задача 3
# Дан список values = [1, 2, 2, 3, 2, 4]
# 1) Посчитай, сколько раз встречается 2
# 2) Удали первое вхождение 2
# 3) Выведи итоговый список
values = [1, 2, 2, 3, 2, 4]
print(f"Два встречается: {len([i for i in values if i == 2])} раз(а)")
values.pop(values.index(2))
print(values)

# Задача 4
# Дан список nums = [7, 3, 9, 1, 3]
# 1) Создай новый отсортированный список по возрастанию (исходный не менять)
# 2) Отсортируй исходный список по убыванию
# 3) Выведи оба списка

nums = [7, 3, 9, 1, 3]
new_nums = sorted(nums)
print(new_nums)
nums.sort(reverse=True)
#print(type(nums.sort(reverse=True)))
#print(type(nums))
print(nums)



# Задача 5
# Дан список scores = [56, 72, 91, 48, 84]
# С помощью list comprehension создай новый список passed,
# где будут только значения >= 60.
scores = [56, 72, 91, 48, 84]
passed = [score for score in scores if score >= 60]
print(passed)




# Задача 6
# Дан список names = ["ann", "bob", "kate"]
# С помощью list comprehension создай список upper_names в верхнем регистре.
# Ожидается: ["ANN", "BOB", "KATE"]
names = ["ann", "bob", "kate"]
upper_names = [name.upper() for name in names]
print(upper_names)


# Задача 7
# Дан список nums = [1, 2, 3, 4, 5, 6]
# Создай список squares_even — квадраты только четных чисел.
# Ожидается: [4, 16, 36]
nums = [1, 2, 3, 4, 5, 6]
squares_even = [num * num for num in nums if num % 2 == 0]
print(squares_even)



# Задача 8
# Дан список words = ["qa", "automation", "test", "python"]
# Создай список word_lengths в формате [("qa", 2), ("automation", 10), ...]
# Можно использовать цикл или list comprehension.
words = ["qa", "automation", "test", "python"]
#word_lengths = [f'("{word}", "{str(len(word))}")' for word in words]
word_lengths = [(word, len(word)) for word in words]
print(word_lengths)

# Задача 9
# Дан список nums = [3, 1, 3, 2, 1, 4, 2]
# Создай новый список unique_nums без дубликатов,
# сохранив порядок первого появления элементов.
# (Решить без set — только списки и условия.)
nums = [3, 1, 3, 2, 1, 4, 2]

unique_nums = [num for i, num in enumerate(nums) if nums.index(num) == i]
print(unique_nums)


# Задача 10
# Дан список transactions = [120, -50, 340, -20, -10, 500]
# Сделай анализ:
# 1) Список доходов (положительные)
# 2) Список расходов (отрицательные)
# 3) Итоговый баланс (sum всех)
# 4) Количество операций каждого типа
# Выведи результаты в читаемом виде.

transactions = [120, -50, 340, -20, -10, 500]

income = [trans for trans in transactions if trans >= 0]
expence = [trans for trans in transactions if trans < 0]
summ_trans = sum(transactions)

print(f"Список доходов: {income}, Список расходов: {expence}, Итоговый баланс: {summ_trans}")
print(f"Количество операций доходов: {len(income)}")
print(f"Количество операций расходов: {len(expence)}")

