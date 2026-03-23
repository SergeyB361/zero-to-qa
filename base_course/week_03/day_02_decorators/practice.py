# Неделя 3, День 2 — Практика: декораторы

# Задание 1
# Напиши декоратор show_start, который:
# - печатает "start"
# - вызывает исходную функцию
# Используй его для функции hello(), которая печатает "hello".
# Напиши код здесь:


def show_start(func):
    def wrapper():
        print("start")
        func()
    return wrapper
    


@show_start
def hello():
    print("hello")

hello()



# Задание 2
# Напиши декоратор show_start_end, который:
# - печатает "start"
# - вызывает исходную функцию
# - печатает "end"
# Используй его для функции bye(), которая печатает "bye".
# Напиши код здесь:

def show_start_end(func):
    def wrapper():
        print("start")
        func()
        print("end")
    return wrapper


@show_start_end
def bye():
    print("bye")

bye()



# Задание 3
# Напиши декоратор log_call, который работает с функцией с аргументами.
# Перед вызовом функции он должен печатать "calling function".
# Используй его для функции multiply(a, b), которая возвращает произведение.
# Затем выведи результат multiply(3, 4).
# Напиши код здесь:

def log_call(func):
    def wrapper(*args):
        print("calling function")
        result = func(*args)
        return result
    return wrapper

@log_call
def  multiply(a, b):
    return a * b


print(multiply(3, 4))


# Задание 4
# Напиши декоратор double_result, который:
# - вызывает исходную функцию
# - получает её результат
# - возвращает результат, умноженный на 2

# Используй его для функции get_number(), которая возвращает 5.
# Затем выведи результат вызова get_number().
# Ожидаемый результат: 10
# Напиши код здесь:


def double_result(func):
    def wrapper():
        result = func() * 2
        return result
    return wrapper


@double_result
def get_number():
    return 5


print(get_number())