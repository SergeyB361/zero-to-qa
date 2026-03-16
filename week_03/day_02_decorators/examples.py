# Неделя 2, День 6 — Примеры


def simple_decorator(func):
    def wrapper():
        print("start")
        func()
        print("finish")
    return wrapper


@simple_decorator
def greet():
    print("hello")


def log_args(func):
    def wrapper(*args, **kwargs):
        print("args:", args)
        print("kwargs:", kwargs)
        return func(*args, **kwargs)
    return wrapper


@log_args
def add(a, b):
    return a + b


if __name__ == "__main__":
    greet()
    print(add(2, 3))
