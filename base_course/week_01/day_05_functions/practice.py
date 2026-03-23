# День 5 — Практика: функции

# Задание 1
# Напиши функцию is_even(number), которая:
# - принимает число
# - возвращает True, если число четное
# - возвращает False, если нечетное
#
# Проверь для: 2, 5, 0, -4
# Напиши код здесь:

#def is_even(number):
#    if number % 2 == 0:
#        chet_is = True
#    else: chet_is = False
#    return chet_is

def is_even(number):
    return number % 2 == 0

print(is_even(2))
print(is_even(5))
print(is_even(0))
print(is_even(-4))

# Задание 2
# Напиши функцию rectangle_area(width, height), которая возвращает площадь прямоугольника.
# Проверь для: (3, 4), (10, 2)
# Напиши код здесь:

def rectangle_area(width, height):
    return width * height

print(rectangle_area(3, 4))
print(rectangle_area(10, 2))

# Задание 3
# Напиши функцию grade(score), которая возвращает:
# - "A" если score >= 90
# - "B" если score >= 75
# - "C" если score >= 60
# - "F" иначе
#
# Проверь для: 95, 80, 61, 40
# Напиши код здесь:

def grade(score):
    kod = ""
    if score >= 90:
        kod = "A"
    elif score >= 75:
        kod = "B"
    elif score >= 60:
        kod = "C"
    else: 
        kod = "F"
    return kod

print(grade(95))
print(grade(80))
print(grade(61))
print(grade(40))


# Задание 4
# Напиши функцию safe_divide(a, b):
# - если b == 0, верни строку "Division by zero"
# - иначе верни результат деления a / b
#
# Проверь для: (10, 2), (7, 0)
# Напиши код здесь:

def safe_divide(a, b):
    if b != 0:
        return a/b
    else:
        return "Division by zero"
    
print(safe_divide(10, 2))
print(safe_divide(7, 0))