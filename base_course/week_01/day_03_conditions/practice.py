# День 3 — Практика: условия

# Задание 1
# Определи категорию HTTP-статус кода через if/elif/else:
#   2xx → "Success"
#   3xx → "Redirect"
#   4xx → "Client Error"
#   5xx → "Server Error"
#   иначе → "Unknown"
#
# Подсказка: используй целочисленное деление: 404 // 100 == 4
#
# Проверь для кодов: 200, 301, 404, 500, 999
# (просто измени значение переменной и запускай каждый раз)
#
# Напиши код здесь:

category = ""
http_status = 301
http_status_group = http_status // 100

if http_status_group == 2:
    category = "Success"
elif http_status_group == 3:
    category = "Redirect"
elif http_status_group == 4:
    category = "Client Error"
elif http_status_group == 5:
    category = "Server Error"
else:
    category = "Unknown"

print(category)




# Задание 2
# Даны переменные пользователя:
user_name = "Sergey"
user_role = "tester"
user_active = True
#
# Выведи:
#   - Если активен и роль "tester": "Активный тестировщик: Sergey"
#   - Если активен, но не тестировщик: "Активный пользователь: Sergey"
#   - Если не активен: "Пользователь неактивен"
#
# Напиши код здесь:

if user_active and user_role == "tester":
    print(f"Активный тестировщик: {user_name}")
elif user_active:
    print(f"Активный пользователь: {user_name}")
else:
    print("Пользователь неактивен")




# Задание 3
# Напиши проверку длины пароля:
#   - менее 6 символов → "Слишком короткий"
#   - 6–7 символов     → "Слабый"
#   - 8–11 символов    → "Нормальный"
#   - 12 и более       → "Надёжный"
#
# Подсказка: len(password) возвращает длину строки
#
# Проверь для: "qwe", "qwerty", "Qwerty1!", "SuperSecretPass"
#
# Напиши код здесь:

password = "SuperSecretPass"
check = ""
length_pass = len(password)

if length_pass < 6:
    check = "Слишком короткий"
elif length_pass <= 7:
    check = "Слабый"
elif length_pass <= 11:
    check = "Нормальный"
else:
    check = "Надёжный"
print(check)


# Задание 4
# Что выведет этот код? Ответь комментарием ПЕРЕД запуском.
#
x = 10
y = 0

print(bool(""))
print(bool(" "))
print(x > 5 and y > 0)
print(x > 5 or y > 0)
print(not x > 5)
print(x > 5 and not y > 0)
# Мои ответы (напиши здесь до запуска):
# False
# True
# False
# True
# False
# True
#
