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


if __name__ == "__main__":
    user = User("Mila")
    admin = Admin("Kate", 2)

    print(user.describe())
    print(admin.describe())
