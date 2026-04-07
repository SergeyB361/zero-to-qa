# День 7 - Мини-проект: User / Admin
#
# Этот файл должен запускаться даже до того, как ты реализуешь все TODO.
# Поэтому здесь оставлен рабочий scaffold:
# - базовые поля уже сохраняются,
# - main() уже показывает demo flow,
# - методы с TODO пока возвращают упрощённый результат.
#
# Твоя задача - постепенно заменить упрощённую реализацию на полноценную
# по требованиям из spec.md.


class User:
    def __init__(self, username: str, email: str) -> None:
        # TODO: сохрани username и email в атрибутах объекта
        # TODO: создай приватный атрибут _active со значением True
        self.username = username
        self.email = email
        self._active = True

    @property
    def is_active(self) -> bool:
        # TODO: верни текущий статус активности пользователя
        return self._active

    def deactivate(self) -> None:
        # TODO: переведи пользователя в неактивное состояние
        self._active = False

    def describe(self) -> str:
        # TODO: верни строку формата:
        # User(username=<username>, active=<True/False>)
        return f"User(username={self.username}, active={self.is_active})"


class Admin(User):
    def __init__(self, username: str, email: str, permissions: list[str]) -> None:
        # TODO: вызови super().__init__(...)
        # TODO: сохрани permissions
        super().__init__(username, email)
        self.permissions = permissions

    def has_permission(self, permission: str) -> bool:
        # TODO: проверь, есть ли permission в списке permissions
        return permission in self.permissions

    def describe(self) -> str:
        # TODO: верни строку формата:
        # Admin(username=<username>, permissions=<count>, active=<True/False>)
        return (
            f"Admin(username={self.username}, permissions={len(self.permissions)}, "
            f"active={self.is_active})"
        )


def print_access_report(user: User) -> None:
    # TODO: напечатай результат user.describe()
    # TODO: если это Admin, дополнительно напечатай:
    # Can delete: <True/False>
    print(user.describe())
    if isinstance(user, Admin):
        print(f"Can delete: {user.has_permission('delete')}")


def main() -> None:
    # TODO:
    # 1. создай обычного пользователя
    # 2. создай администратора
    # 3. выведи отчёт для обоих
    # 4. деактивируй обычного пользователя
    # 5. снова выведи отчёт
    user = User("anna", "anna@example.com")
    admin = Admin("root", "root@example.com", ["read", "write", "delete"])

    print("=== Access report ===")
    print_access_report(user)
    print_access_report(admin)

    print()
    print("=== After deactivation ===")
    user.deactivate()
    print_access_report(user)


if __name__ == "__main__":
    main()
