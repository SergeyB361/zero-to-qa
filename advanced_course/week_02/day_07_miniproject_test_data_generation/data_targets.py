USER_ROLES = {"user", "admin", "guest"}
ORDER_STATUSES = {"new", "paid", "cancelled"}


def validate_user(email: str, role: str) -> bool:
    return "@" in email and role in USER_ROLES


def validate_order(amount: int, status: str) -> bool:
    return 0 < amount <= 10000 and status in ORDER_STATUSES
