# Неделя 3, День 5 — Практика: logging

import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

# Задание 1
# Выведи через logging.info сообщение:
# "Program started"

logging.info("Program started")


# Задание 2
# Выведи через logging.warning сообщение:
# "Low memory"

logging.warning("Low memory")


# Задание 3
# Напиши функцию greet(name), которая:
# - логирует через logging.info сообщение "Greeting user: <name>"
# - возвращает строку "Hello, <name>"
# Затем выведи результат greet("Sergey")

def greet(name):
    logging.info(f"Greeting user: {name}")
    return f"Hello, {name}"

print(greet("Sergey"))


# Задание 4
# Напиши функцию safe_div(a, b), которая:
# - логирует попытку деления через logging.info
# - если b == 0, логирует ошибку через logging.error и возвращает строку "division by zero"
# - иначе возвращает результат деления
# Затем выведи результат safe_div(10, 0)


def safe_div(a, b):
    logging.info(f"safe_div: {a} / {b}")
    if b == 0:
        logging.error("division by zero")
        result =  "division by zero"
    else:
        result = a / b
    return result


print(safe_div(10, 0))