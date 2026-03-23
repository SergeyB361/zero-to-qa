def can_access(role: str, resource: str) -> bool:
    rules = {"admin": {"users", "orders"}, "user": {"orders"}}
    return resource in rules.get(role, set())


if __name__ == "__main__":
    print(can_access("admin", "users"))
    print(can_access("user", "users"))
