# День 6 — Практика: функции (продвинуто)

# Задание 1
# Напиши функцию welcome(name, role="QA Engineer"), которая возвращает строку:
# "Добро пожаловать, <name>! Роль: <role>"
#
# Проверь для:
# welcome("Sergey")
# welcome("Sergey", "SDET")
# Напиши код здесь:

def welcome(name, role="QA Engineer"):
    return (f"Добро пожаловать, {name}! Роль: {role}")

print(welcome("Sergey"))
print(welcome("Sergey","SDET"))


# Задание 2
# Напиши функцию average(*numbers), которая:
# - принимает любое количество чисел
# - возвращает их среднее арифметическое
# - если аргументов нет, возвращает 0
#
# Проверь для:
# average(2, 4, 6)
# average(10, 20)
# average()
# Напиши код здесь:

def average(*numbers):
    if (numbers) == ():
        average_summ = 0
    else: 
        average_summ = sum(numbers)/ len(numbers)
    return average_summ

print(average(2,4,6))
print(average())
print(average(10,20))




# Задание 3
# Напиши функцию format_profile(**kwargs), которая собирает строку вида:
# "name=Sergey, role=QA, level=junior"
#
# Требования:
# - ключи выводить в алфавитном порядке
# - пары "key=value" разделять запятой и пробелом
#
# Проверь для:
# format_profile(name="Sergey", role="QA", level="junior")
# Напиши код здесь:

def format_profile(**kwargs):
    person = (kwargs)
    stroka = []
    for key in sorted(person):
        stroka.append(f"{key}={person[key]}")
    return ", ".join(stroka)

print(format_profile(name="Sergey", role="QA", level="junior"))




# Задание 4
# Дан список словарей users:
users = [
    {"name": "Alex", "score": 78},
    {"name": "Mila", "score": 92},
    {"name": "John", "score": 85},
]
#
# Отсортируй users по score по убыванию с помощью sorted(..., key=lambda ...)
# и выведи результат.
# Напиши код здесь:

user_score = sorted(users, key=lambda u: u["score"], reverse=True)
print(user_score)
