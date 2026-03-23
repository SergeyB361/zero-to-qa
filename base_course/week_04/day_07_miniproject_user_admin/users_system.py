# День 7 — Мини-проект: User / Admin


class User:
    def __init__(self, username: str, email: str) -> None:
        # TODO: сохрани username и email в атрибутах объекта
        # TODO: создай приватный атрибут _active со значением True
        pass

    @property
    def is_active(self) -> bool:
        # TODO: верни текущий статус активности пользователя
        raise NotImplementedError

    def deactivate(self) -> None:
        # TODO: переведи пользователя в неактивное состояние
        raise NotImplementedError

    def describe(self) -> str:
        # TODO: верни строку формата:
        # User(username=<username>, active=<True/False>)
        raise NotImplementedError


class Admin(User):
    def __init__(self, username: str, email: str, permissions: list[str]) -> None:
        # TODO: вызови super().__init__(...)
        # TODO: сохрани permissions
        super().__init__(username, email)
        raise NotImplementedError

    def has_permission(self, permission: str) -> bool:
        # TODO: проверь, есть ли permission в списке permissions
        raise NotImplementedError

    def describe(self) -> str:
        # TODO: верни строку формата:
        # Admin(username=<username>, permissions=<count>, active=<True/False>)
        raise NotImplementedError


def print_access_report(user: User) -> None:
    # TODO: напечатай результат user.describe()
    # TODO: если это Admin, дополнительно напечатай:
    # Can delete: <True/False>
    raise NotImplementedError


def main() -> None:
    # TODO:
    # 1. создай обычного пользователя
    # 2. создай администратора
    # 3. выведи отчёт для обоих
    # 4. деактивируй обычного пользователя
    # 5. снова выведи отчёт
    raise NotImplementedError


if __name__ == "__main__":
    main()
