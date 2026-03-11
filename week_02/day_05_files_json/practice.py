# Неделя 2, День 5 — Практика: файлы и JSON

import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Задание 1
# Создай файл day5_note.txt в папке текущего урока и запиши в него 3 строки:
# 1) "Python"
# 2) "QA"
# 3) "Automation"
# Затем прочитай файл и выведи содержимое целиком.
# Напиши код здесь:

print()

# Задание 2
# Создай словарь user_data:
# {
#   "name": "sergey",
#   "age": 28,
#   "skills": ["python", "pytest", "api"]
# }
#
# Запиши его в файл user_data.json (красиво, с indent=2),
# затем прочитай обратно и выведи значение ключа "skills".
# Напиши код здесь:


# Задание 3
# Дан файл logs.txt (создай его сам в коде) со строками:
# INFO: start
# ERROR: timeout
# INFO: retry
# ERROR: bad gateway
#
# Посчитай, сколько строк начинается с "ERROR" и выведи число.
# Напиши код здесь:


# Задание 4
# Создай JSON-файл products.json со списком товаров:
# [
#   {"name": "Keyboard", "price": 2500},
#   {"name": "Mouse", "price": 1200},
#   {"name": "Monitor", "price": 15000}
# ]
#
# Прочитай файл и выведи:
# 1) количество товаров
# 2) среднюю цену
# Напиши код здесь:
