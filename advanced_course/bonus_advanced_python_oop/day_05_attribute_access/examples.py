class EventPayloadView:
    def __init__(self, payload: dict[str, object]) -> None:
        self.payload = payload

    def __getattr__(self, name: str) -> object:
        if name in self.payload:
            return self.payload[name]
        raise AttributeError(f"{type(self).__name__!s} has no attribute {name!r}")


class AccessLogger:
    def __init__(self, service_name: str, status: str) -> None:
        object.__setattr__(self, "_access_log", [])
        self.service_name = service_name
        self.status = status

    def __getattribute__(self, name: str) -> object:
        if name not in {"_access_log", "access_log", "__dict__", "__class__"}:
            log = object.__getattribute__(self, "_access_log")
            log.append(name)
        return object.__getattribute__(self, name)

    @property
    def access_log(self) -> list[str]:
        return list(object.__getattribute__(self, "_access_log"))


class NormalizedUser:
    def __setattr__(self, name: str, value: object) -> None:
        if isinstance(value, str):
            value = value.strip()
            if name == "email":
                value = value.lower()
        object.__setattr__(self, name, value)


if __name__ == "__main__":
    view = EventPayloadView({"status": "open", "priority": "high"})
    print("=== __getattr__ fallback ===")
    print(view.status)
    print(view.priority)
    print()

    logger = AccessLogger("task-service", "healthy")
    print("=== __getattribute__ logs reads ===")
    print(logger.service_name)
    print(logger.status)
    print(logger.access_log)
    print()

    user = NormalizedUser()
    user.email = "  USER@EXAMPLE.COM  "
    user.name = "  Sergey  "
    print("=== __setattr__ normalizes values ===")
    print(user.email)
    print(user.name)