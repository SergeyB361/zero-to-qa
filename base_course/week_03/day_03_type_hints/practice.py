# Неделя 3, День 3 — Практика: type hints

#from typing import Optional

# Задание 1
# Напиши функцию multiply(a, b), которая принимает два int
# и возвращает их произведение.
# Добавь type hints.


def multiply (a: int, b: int) -> int:
    return a * b

print(multiply(2, 3))



# Задание 2
# Напиши функцию make_label(name, priority), которая:
# - принимает name как str
# - принимает priority как int
# - возвращает str
# Формат строки: "<name>: <priority>"
# Добавь type hints.

def make_label(name: str, priority: int) -> str:
    return f"{name}: {priority}"

print(make_label("Alex", 1))



# Задание 3
# Напиши функцию get_tags(), которая возвращает список строк:
# ["smoke", "api", "regression"]
# Добавь type hints.

def get_tags() -> list[str]:
    return ["smoke", "api", "regression"]

print(get_tags())



# Задание 4
# Напиши функцию normalize_title(title), которая:
# - принимает Optional[str]
# - если title is None, возвращает "untitled"
# - иначе возвращает title в верхнем регистре
# Добавь type hints.


def normalize_title(title: str | None) -> str:
    if title is None:
        status = "untitled"
    else:
        status = title.upper()
    return status

print(normalize_title("asdf"))
print(normalize_title(None))






