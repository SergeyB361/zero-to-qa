USERS = {
    "valid_user": {"email": "qa@example.com", "role": "user", "active": True},
    "blocked_user": {"email": "blocked@example.com", "role": "user", "active": False},
}

ORDERS = {
    "new_order": {"amount": 100, "status": "new"},
    "discount_order": {"amount": 80, "status": "paid", "discount": 20},
}


if __name__ == "__main__":
    print(USERS["valid_user"])
    print(ORDERS["discount_order"])
