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

with open(BASE_DIR/"day5_note.txt", "w") as f:
    f.write("""1) "Python"
2) "QA"
3) "Automation"
""")

with open(BASE_DIR/"day5_note.txt", "r") as f:
    content = f.read()

print(content)
# print(BASE_DIR)


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
# import json

user_data = {
   "name": "sergey",
   "age": 28,
   "skills": ["python", "pytest", "api"]
}

with open (BASE_DIR/"user_data.json", "w") as f:
    json.dump(user_data, f, ensure_ascii=False, indent=2)

with open(BASE_DIR/"user_data.json", "r") as f:
    data_from_file = json.load(f)
    print(data_from_file["skills"])


# Задание 3
# Дан файл logs.txt (создай его сам в коде) со строками:
# INFO: start
# ERROR: timeout
# INFO: retry
# ERROR: bad gateway
#
# Посчитай, сколько строк начинается с "ERROR" и выведи число.
# Напиши код здесь:

lines = ["INFO: start", "ERROR: timeout", "INFO: retry", "ERROR: bad gateway"]

with open(BASE_DIR/"logs.txt", "w") as f:
    for line in lines:
        f.write(f"{line}\n")

with open(BASE_DIR/"logs.txt", "r") as f:
    lines_from_file = f.readlines()

# print(lines_from_file[:])
line_error = 0

for line in lines_from_file:
    if line.startswith("ERROR"): # лучше без == True:
        line_error +=1
    
print(f"""строк начинается с "ERROR" {line_error}""")


#второй лаконичный вариант:
#==========================
lines = ["INFO: start", "ERROR: timeout", "INFO: retry", "ERROR: bad gateway"]

with open(BASE_DIR / "logs.txt", "w") as f:
    f.writelines(f"{line}\n" for line in lines)

with open(BASE_DIR / "logs.txt", "r") as f:
    lines_from_file = f.readlines()

line_error = sum(1 for line in lines_from_file if line.startswith("ERROR"))

print(f'строк начинается с "ERROR": {line_error}')



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

goods = [ 
    {"name": "Keyboard", "price": 2500},
    {"name": "Mouse", "price": 1200},
    {"name": "Monitor", "price": 15000}
]

with open(BASE_DIR/"products.json", "w") as f:
    json.dump(goods, f, indent=2)

with open(BASE_DIR/"products.json", "r") as f:
    products = json.load(f)

count = len(products)
total = sum(item["price"] for item in products)
avg = total / count

print(count)
print(round(avg,2))
