# Неделя 5, День 1 — Примеры


def sum_two_numbers(a: int, b: int) -> int:
    return a + b


def show_examples() -> None:
    print("Unit test example target:", sum_two_numbers(2, 3))
    print("Integration example: API client + database check")
    print("E2E example: user logs in and creates an order")


if __name__ == "__main__":
    show_examples()
