# Неделя 4, День 1 — Примеры


class User:
    def __init__(self, name: str, role: str) -> None:
        self.name = name
        self.role = role


class TestCase:
    def __init__(self, title: str, priority: str) -> None:
        self.title = title
        self.priority = priority


if __name__ == "__main__":
    user = User("Sergey", "tester")
    print(user.name, user.role)

    case = TestCase("Login works", "high")
    print(case.title, case.priority)
