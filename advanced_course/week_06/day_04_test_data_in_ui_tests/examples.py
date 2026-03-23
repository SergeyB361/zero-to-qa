def make_unique_username(seed: int) -> str:
    return f"ui_user_{seed}"


if __name__ == "__main__":
    print(make_unique_username(42))
