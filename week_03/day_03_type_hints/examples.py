# Неделя 3, День 3 — Примеры

from typing import Optional


def add(a: int, b: int) -> int:
    return a + b


def format_user(name: str, age: int) -> str:
    return f"{name} ({age})"


def get_statuses() -> list[str]:
    return ["new", "ready", "done"]


def get_scores() -> dict[str, int]:
    return {"api": 90, "ui": 85}


def normalize_name(name: Optional[str]) -> str:
    if name is None:
        return "unknown"
    return name.strip().title()


if __name__ == "__main__":
    print(add(2, 3))
    print(format_user("Sergey", 28))
    print(get_statuses())
    print(get_scores())
    print(normalize_name(None))
