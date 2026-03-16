# Неделя 2, День 6 — Примеры

from pathlib import Path

BASE_DIR = Path(__file__).parent


def demo_int_parse(value: str) -> None:
    try:
        number = int(value)
    except ValueError:
        print("Ошибка: это не целое число")
    else:
        print("Успех:", number)


def demo_division(a: int, b: int) -> None:
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")


def demo_file_read(filename: str) -> None:
    try:
        with open(BASE_DIR / filename, "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("Ошибка: файл не найден")


def validate_age(age: int) -> None:
    if age < 0:
        raise ValueError("Возраст не может быть отрицательным")
    print("Возраст принят:", age)


if __name__ == "__main__":
    demo_int_parse("123")
    demo_int_parse("abc")

    demo_division(10, 2)
    demo_division(10, 0)

    demo_file_read("sample.txt")

    try:
        validate_age(-1)
    except ValueError as err:
        print("Ошибка валидации:", err)
