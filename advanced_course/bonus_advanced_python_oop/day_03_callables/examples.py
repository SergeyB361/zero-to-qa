class MinLengthValidator:
    def __init__(self, min_length: int) -> None:
        self.min_length = min_length

    def __call__(self, value: str) -> bool:
        return len(value) >= self.min_length


class StatusFilter:
    def __init__(self, allowed_status: str) -> None:
        self.allowed_status = allowed_status

    def __call__(self, task: dict[str, str]) -> bool:
        return task.get("status") == self.allowed_status


class RequestCounter:
    def __init__(self) -> None:
        self.calls = 0

    def __call__(self) -> int:
        self.calls += 1
        return self.calls


if __name__ == "__main__":
    print("=== Validator ===")
    validator = MinLengthValidator(8)
    print(callable(validator))
    print(validator("secret123"))
    print(validator("short"))
    print()

    print("=== Filter ===")
    tasks = [
        {"id": "TASK-1", "status": "open"},
        {"id": "TASK-2", "status": "done"},
        {"id": "TASK-3", "status": "open"},
    ]
    is_open = StatusFilter("open")
    filtered = [task for task in tasks if is_open(task)]
    print(filtered)
    print()

    print("=== Stateful callable ===")
    counter = RequestCounter()
    print(counter())
    print(counter())
    print(counter())
