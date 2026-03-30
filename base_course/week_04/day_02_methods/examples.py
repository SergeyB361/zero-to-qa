# Неделя 4, День 2 — Примеры


class User:
    total = 0

    def __init__(self, name: str) -> None:
        self.name = name
        User.total += 1

    def greet(self) -> str:
        # Обычный метод работает с конкретным объектом.
        return f"Hello, {self.name}"

    @classmethod
    def get_total(cls) -> int:
        # Classmethod работает с классом и его общими данными.
        return cls.total

    @staticmethod
    def is_valid_name(name: str) -> bool:
        # Staticmethod не использует ни объект, ни класс.
        return len(name) >= 2


class Counter:
    total_created = 0

    def __init__(self, start: int) -> None:
        self.value = start
        Counter.total_created += 1

    def increment(self) -> int:
        self.value += 1
        return self.value

    @classmethod
    def get_created_count(cls) -> int:
        return cls.total_created

    @staticmethod
    def is_positive(number: int) -> bool:
        return number > 0


if __name__ == "__main__":
    first = User("Ann")
    second = User("Bob")

    print("=== User ===")
    print(first.greet())
    print(User.get_total())
    print(User.is_valid_name("A"))
    print(User.is_valid_name("Ann"))

    counter = Counter(10)

    print("=== Counter ===")
    print(counter.increment())
    print(counter.increment())
    print(Counter.get_created_count())
    print(Counter.is_positive(5))
    print(Counter.is_positive(-2))
