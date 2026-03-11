# Неделя 2, День 4 — Практика: строки

# Задание 1
# Дана строка s = "  Python QA  "
#
# Сделай:
# 1) Удали пробелы по краям
# 2) Переведи в нижний регистр
# 3) Выведи длину полученной строки
# Напиши код здесь:
s = "  Python QA  "
s = s.strip()
s = s.lower()
print(len(s))


# Задание 2
# Дана строка log = "ERROR 500 POST /login"
#
# Сделай:
# 1) Проверь, содержит ли строка "500"
# 2) Проверь, начинается ли строка с "ERROR"
# 3) Найди позицию подстроки "POST"
# Напиши код здесь:

log = "ERROR 500 POST /login"

is_500 = log.find("500")
if is_500 == -1:
    print("Не содержит 500")
else:
    print("Cодержит 500")

is_error = log.find("ERROR")
if is_error == -1:
    print("Не содержит ERROR")
else:
    print("Cодержит ERROR")

include_post = log.find("POST")
print(include_post)


# Задание 3
# Дана строка users_line = "ann,bob,kate"
#
# Сделай:
# 1) Разбей строку на список имен
# 2) Собери новую строку через "; " как разделитель
# Ожидается: "ann; bob; kate"
# Напиши код здесь:

users_line = "ann,bob,kate"
user_names = users_line.split(",")
new_line = [user_name for user_name in user_names]
print("; ".join(new_line))


# Задание 4
# Дана строка phrase = "qa automation engineer"
#
# Сделай:
# 1) Преобразуй в Title Case
# 2) Замени "engineer" на "specialist"
# 3) Выведи итоговую строку
# Напиши код здесь:

phrase = "qa automation engineer"
phrase = phrase.title()
phrase = phrase.replace("Engineer", "Specialist")
print(phrase)
