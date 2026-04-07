# Неделя 4, День 1 — Примеры


class User:
    default_role = "tester"
    total_created = 0

    def __init__(self, name: str, role: str | None = None) -> None:
        self.name = name
        self.role = role or User.default_role
        User.total_created += 1


class TestCase:
    project = "zero-to-qa"

    def __init__(self, title: str, priority: str) -> None:
        self.title = title
        self.priority = priority


if __name__ == "__main__":
    first = User("Sergey")
    second = User("Anna", "lead tester")

    print(first.name, first.role)
    print(second.name, second.role)
    print(User.total_created)

    case = TestCase("Login works", "high")
    print(case.title, case.priority)
    print(TestCase.project)
