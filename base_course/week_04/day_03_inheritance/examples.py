# Неделя 4, День 3 — Примеры


class User:
    def __init__(self, name: str) -> None:
        self.name = name

    def describe(self) -> str:
        return f"User: {self.name}"


class Admin(User):
    def __init__(self, name: str, level: int) -> None:
        super().__init__(name)
        self.level = level

    def describe(self) -> str:
        return f"Admin: {self.name}, level={self.level}"


def print_description(obj: User) -> None:
    # Один и тот же вызов работает для User и Admin.
    print(obj.describe())


if __name__ == "__main__":
    user = User("Mila")
    admin = Admin("Kate", 2)

    print_description(user)
    print_description(admin)

    print(isinstance(admin, Admin))
    print(isinstance(admin, User))
    print(issubclass(Admin, User))
