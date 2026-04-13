# Bonus Advanced Python OOP, День 5 - __getattr__, __getattribute__, __setattr__
#
# Здесь 4 задания. Файл запускается уже сейчас,
# но логика перехвата атрибутов пока неполная.


# Задание 1
# Реализуй fallback через __getattr__:
# если имя есть в payload, верни значение из словаря.
class ApiResponseView:
    def __init__(self, payload: dict[str, object]) -> None:
        self.payload = payload

    def __getattr__(self, name: str) -> object:
        # TODO:
        # if name in self.payload:
        #     return self.payload[name]
        raise AttributeError(f"{type(self).__name__!s} has no attribute {name!r}")


# Задание 2
# Реализуй нормализацию через __setattr__:
# - все строки trim
# - email переводить в lowercase
class NormalizedAccount:
    def __setattr__(self, name: str, value: object) -> None:
        # TODO:
        # if isinstance(value, str):
        #     ...
        object.__setattr__(self, name, value)


# Задание 3
# Реализуй безопасный tracer через __getattribute__.
# Нужно записывать имена прочитанных атрибутов в _reads.
class ReadTracker:
    def __init__(self, service_name: str, region: str) -> None:
        object.__setattr__(self, "_reads", [])
        self.service_name = service_name
        self.region = region

    def __getattribute__(self, name: str) -> object:
        # TODO:
        # if name not in {...}:
        #     reads = object.__getattribute__(self, "_reads")
        #     reads.append(name)
        return object.__getattribute__(self, name)

    @property
    def reads(self) -> list[str]:
        return list(object.__getattribute__(self, "_reads"))


# Задание 4
# Подумай, почему BrokenTracer опасен.
# Если внутри __getattribute__ обратиться к self.some_field,
# можно получить бесконечную рекурсию.
class BrokenTracer:
    def __init__(self) -> None:
        self.value = 10

    def __getattribute__(self, name: str) -> object:
        # Здесь нельзя писать self.value.
        return object.__getattribute__(self, name)


if __name__ == "__main__":
    print("=== Current scaffold output ===")

    response = ApiResponseView({"status": "ok", "duration_ms": 42})
    try:
        print("response.status ->", response.status)
    except AttributeError as error:
        print("response.status failed:", error)

    account = NormalizedAccount()
    account.email = "  USER@EXAMPLE.COM  "
    account.name = "  Sergey  "
    print("account.email ->", account.email)
    print("account.name ->", account.name)

    tracker = ReadTracker("task-service", "eu-west")
    print("tracker.service_name ->", tracker.service_name)
    print("tracker.region ->", tracker.region)
    print("tracker.reads ->", tracker.reads)