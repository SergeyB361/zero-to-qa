# Неделя 2, День 1 — Практика: списки

# Задание 1
# Дан список statuses:
statuses = [200, 404, 500, 200, 301, 404]
#
# Сделай следующее:
# 1) Выведи первый и последний элемент списка
# 2) Посчитай, сколько раз встречается 404
# 3) Добавь в конец 201
# 4) Выведи итоговый список
# Напиши код здесь:

# 1)
print(statuses[0])
print(statuses[-1])

# 2) # Вариант A: через list comprehension
st_404 = 0
st_404 = len([status for status in statuses if status == 404])
print(st_404)

# 2) # Вариант B: через цикл for
st_404 = 0
for status in statuses:
    if status == 404:
        st_404 = st_404 + 1
print(st_404)

# 3)
statuses.append(201)

# 4)
print(statuses)



# Задание 2
# Дан список nums = [7, 2, 9, 2, 1]
#
# Сделай:
# 1) Создай новый отсортированный список по возрастанию (исходный не менять)
# 2) Отсортируй исходный список по убыванию
# 3) Выведи оба списка
# Напиши код здесь:

nums = [7, 2, 9, 2, 1]
nums_sort = sorted(nums)
nums.sort(reverse=True)

print(nums)
print(nums_sort)




# Задание 3
# Используя list comprehension, создай список квадратов чисел от 1 до 10,
# но только для четных чисел.
#
# Ожидается: [4, 16, 36, 64, 100]
# Напиши код здесь:

square_list = []
square_list = list(x*x for x in range(1,11) if x % 2 == 0)
# square_list = [x * x for x in range(1, 11) if x % 2 == 0] вариант без list()
print(square_list)


# Задание 4
# Дан список users = ["ann", "bob", "kate"]
#
# С помощью list comprehension создай новый список
# в формате: ["user: ann", "user: bob", "user: kate"]
# Напиши код здесь:

users = ["ann", "bob", "kate"]

#new_users = [] - можно убрать
new_users = [f"user: {x}" for x in users]
print(new_users)