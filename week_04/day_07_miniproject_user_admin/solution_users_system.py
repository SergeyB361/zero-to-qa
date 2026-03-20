# Day 7 - Reference solution: User / Admin mini-project


class User:
    def __init__(self, username: str, email: str) -> None:
        self.username = username
        self.email = email
        self._active = True

    @property
    def is_active(self) -> bool:
        return self._active

    def deactivate(self) -> None:
        self._active = False

    def describe(self) -> str:
        return f"User(username={self.username}, active={self.is_active})"

    def __str__(self) -> str:
        return self.describe()


class Admin(User):
    def __init__(self, username: str, email: str, permissions: list[str]) -> None:
        super().__init__(username, email)
        self.permissions = permissions

    def has_permission(self, permission: str) -> bool:
        return permission in self.permissions

    def describe(self) -> str:
        count = len(self.permissions)
        return (
            f"Admin(username={self.username}, "
            f"permissions={count}, active={self.is_active})"
        )

    def __str__(self) -> str:
        return self.describe()


def print_access_report(user: User) -> None:
    print(user.describe())
    if isinstance(user, Admin):
        print(f"Can delete: {user.has_permission('delete')}")


def main() -> None:
    user = User("anna", "anna@example.com")
    admin = Admin("root", "root@example.com", ["read", "write", "delete"])

    print_access_report(user)
    print_access_report(admin)

    user.deactivate()
    print_access_report(user)


if __name__ == "__main__":
    main()
