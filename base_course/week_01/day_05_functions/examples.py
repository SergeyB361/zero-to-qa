# День 5 — Примеры: функции

def add(a, b):
    return a + b


def is_even(number):
    return number % 2 == 0


def print_user(name, age):
    print(f"Пользователь: {name}, возраст: {age}")


print(add(10, 5))          # 15
print(is_even(4))          # True
print(is_even(7))          # False
print_user("Sergey", 28)
