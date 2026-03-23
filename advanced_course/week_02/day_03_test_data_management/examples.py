COMMON_ROLES = ["user", "admin", "guest"]
PLAN_PRICES = {"basic": 10, "pro": 25}


def make_unique_email(seed: int) -> str:
    return f"user{seed}@example.com"


def build_profile(seed: int, role: str = "user") -> dict[str, object]:
    return {"email": make_unique_email(seed), "role": role, "plan": "basic"}


if __name__ == "__main__":
    print(COMMON_ROLES)
    print(build_profile(7, role="admin"))
