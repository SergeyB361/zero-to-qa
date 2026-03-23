def ci_suite(kind: str) -> list[str]:
    if kind == "smoke":
        return ["auth", "checkout"]
    return ["auth", "checkout", "profile", "orders"]


if __name__ == "__main__":
    print(ci_suite("smoke"))
