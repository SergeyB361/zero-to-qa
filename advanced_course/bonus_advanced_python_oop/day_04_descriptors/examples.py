class NonEmptyString:
    def __set_name__(self, owner: type, name: str) -> None:
        self.storage_name = "_" + name

    def __get__(self, instance: object, owner: type | None = None) -> object:
        if instance is None:
            return self
        return getattr(instance, self.storage_name)

    def __set__(self, instance: object, value: str) -> None:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("value must not be empty")
        setattr(instance, self.storage_name, cleaned)


class PositiveInt:
    def __set_name__(self, owner: type, name: str) -> None:
        self.storage_name = "_" + name

    def __get__(self, instance: object, owner: type | None = None) -> object:
        if instance is None:
            return self
        return getattr(instance, self.storage_name)

    def __set__(self, instance: object, value: int) -> None:
        if value <= 0:
            raise ValueError("value must be positive")
        setattr(instance, self.storage_name, value)


class RetryPolicy:
    service_name = NonEmptyString()
    retries = PositiveInt()

    def __init__(self, service_name: str, retries: int) -> None:
        self.service_name = service_name
        self.retries = retries


if __name__ == "__main__":
    policy = RetryPolicy(" task-service ", 3)

    print("=== descriptor-backed fields ===")
    print(policy.service_name)
    print(policy.retries)
    print()

    print("=== descriptor lives on class ===")
    print(type(RetryPolicy.service_name).__name__)
    print(type(RetryPolicy.retries).__name__)
    print()

    print("=== validation ===")
    try:
        policy.retries = 0
    except ValueError as error:
        print(error)

    try:
        policy.service_name = "   "
    except ValueError as error:
        print(error)