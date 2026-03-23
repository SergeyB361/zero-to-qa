# Неделя 3, День 4 — Практика: регулярные выражения

import re

# Задание 1
# Дан текст: "User id: 12345"
# Найди первое число через re.search и выведи его.

text = "User id: 12345"
number_first = re.search(r'\d+', text)
print(int(number_first.group()))


# Задание 2
# Дан текст: "Codes: 200 404 500"
# Найди все числа через re.findall и выведи список.

text = "Codes: 200 404 500"
number_all = re.findall(r'\d+', text)
print(number_all)


# Задание 3
# Дан email: "qa.team@example.com"
# Проверь через regex, что строка похожа на email.
# Выведи True или False.

email = "qa.team@example.com"
is_email = re.match(r'[\w.]+@[\w.]+\.\w+', email)
#print(is_email.group())
print(bool(is_email))

# Задание 4
# Дан текст: "Order 123 created at 10:45"
# Замени все цифры на символ "X" через re.sub.
# Выведи результат.

text = "Order 123 created at 10:45"
text_change = re.sub(r'\d+', "X", text)

print(text_change)
