# Bonus Advanced Python OOP, День 4 - Дескрипторы и property
#
# В этом файле нужно реализовать 4 задания.
# Файл запускается уже сейчас, но descriptor-логика пока слишком слабая.


# Задание 1
# Реализуй __set__ так, чтобы строка:
# - очищалась через strip()
# - не могла быть пустой
class NonEmptyString:
    def __set_name__(self, owner: type, name: str) -> None:
        self.storage_name = "_" + name

    def __get__(self, instance: object, owner: type | None = None) -> object:
        if instance is None:
            return self
        return getattr(instance, self.storage_name, "")

    def __set__(self, instance: object, value: str) -> None:
        # TODO:
        # cleaned = value.strip()
        # if not cleaned:
        #     raise ValueError(...)
        # setattr(instance, self.storage_name, cleaned)
        setattr(instance, self.storage_name, value)


# Задание 2
# Реализуй PositiveInt так, чтобы значение было > 0.
class PositiveInt:
    def __set_name__(self, owner: type, name: str) -> None:
        self.storage_name = "_" + name

    def __get__(self, instance: object, owner: type | None = None) -> object:
        if instance is None:
            return self
        return getattr(instance, self.storage_name, 0)

    def __set__(self, instance: object, value: int) -> None:
        # TODO:
        # if value <= 0:
        #     raise ValueError(...)
        setattr(instance, self.storage_name, value)


# Задание 3
# Реализуй ChoiceField так, чтобы значение входило в allowed_values.
class ChoiceField:
    def __init__(self, *allowed_values: str) -> None:
        self.allowed_values = set(allowed_values)

    def __set_name__(self, owner: type, name: str) -> None:
        self.storage_name = "_" + name

    def __get__(self, instance: object, owner: type | None = None) -> object:
        if instance is None:
            return self
        return getattr(instance, self.storage_name, None)

    def __set__(self, instance: object, value: str) -> None:
        # TODO:
        # if value not in self.allowed_values:
        #     raise ValueError(...)
        setattr(instance, self.storage_name, value)


# Задание 4
# Доведи ServiceConfig до корректной работы descriptor-полей.
class ServiceConfig:
    name = NonEmptyString()
    retries = PositiveInt()
    status = ChoiceField("draft", "active", "disabled")

    def __init__(self, name: str, retries: int, status: str) -> None:
        self.name = name
        self.retries = retries
        self.status = status


if __name__ == "__main__":
    print("=== Current scaffold output ===")

    config = ServiceConfig(" task-service ", 3, "draft")
    print("name ->", config.name)
    print("retries ->", config.retries)
    print("status ->", config.status)
    print()

    try:
        config.name = "   "
        print("empty name was accepted")
    except ValueError as error:
        print("empty name rejected:", error)

    try:
        config.retries = 0
        print("zero retries was accepted")
    except ValueError as error:
        print("zero retries rejected:", error)

    try:
        config.status = "archived"
        print("invalid status was accepted")
    except ValueError as error:
        print("invalid status rejected:", error)