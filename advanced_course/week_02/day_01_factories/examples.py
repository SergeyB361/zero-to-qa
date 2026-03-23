def make_user(email: str = "qa@example.com", role: str = "user", active: bool = True) -> dict[str, object]:
    return {"email": email, "role": role, "active": active}


def make_order(amount: int = 100, status: str = "new") -> dict[str, object]:
    return {"amount": amount, "status": status}


if __name__ == "__main__":
    print(make_user())
    print(make_user(role="admin"))
    print(make_order(amount=250, status="paid"))
