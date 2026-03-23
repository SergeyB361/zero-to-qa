# Неделя 2, День 3 — Практика: словари

# Задание 1
# Дан словарь user:
user = {"name": "ann", "age": 25, "role": "tester"}
#
# Сделай:
# 1) Выведи значение ключа "name"
# 2) Добавь ключ "active" со значением True
# 3) Измени "age" на 26
# 4) Выведи итоговый словарь
# Напиши код здесь:

print(user["name"])
user["active"] = True
user["age"] = 26
print(user) 

# Задание 2
# Дан словарь status_counts = {200: 120, 404: 8, 500: 2}
#
# Сделай:
# 1) Выведи количество для 404
# 2) Безопасно получи значение для 301 (если нет, вернуть 0)
# 3) Добавь 301 со значением 5
# 4) Выведи итоговый словарь
# Напиши код здесь:

status_counts = {200: 120, 404: 8, 500: 2}
print(status_counts[404])
print(status_counts.get(301, 0))
status_counts[301] = 5
print(status_counts)


# Задание 3
# Дан словарь product = {"name": "Keyboard", "price": 2500, "stock": 7}
#
# Выведи все пары ключ-значение в формате:
# name -> Keyboard
# price -> 2500
# ...
# Напиши код здесь:

product = {"name": "Keyboard", "price": 2500, "stock": 7}

for key, value in product.items():
    print(f"{key} -> {value}")



# Задание 4
# Дан вложенный словарь profile:
profile = {
    "username": "qa_user",
    "stats": {"tests": 52, "bugs": 11}
}
#
# Сделай:
# 1) Выведи количество тестов
# 2) Увеличь количество bugs на 1
# 3) Выведи обновленный profile
# Напиши код здесь:

kolvo_test = profile['stats']['tests']
print(kolvo_test)
profile['stats']['bugs'] +=1
print(profile)