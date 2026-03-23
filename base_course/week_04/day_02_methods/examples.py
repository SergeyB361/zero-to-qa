# Неделя 4, День 2 — Примеры


class User:
    total = 0

    def __init__(self, name: str) -> None:
        self.name = name
        User.total += 1

    def greet(self) -> str:
        return f"Hello, {self.name}"

    @classmethod
    def get_total(cls) -> int:
        return cls.total

    @staticmethod
    def is_adult(age: int) -> bool:
        return age >= 18


if __name__ == "__main__":
    first = User("Ann")
    second = User("Bob")

    print(first.greet())
    print(User.get_total())
    print(User.is_adult(20))
