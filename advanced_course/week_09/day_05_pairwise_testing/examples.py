def pairwise_seed() -> list[tuple[str, str]]:
    return [("chromium", "admin"), ("firefox", "user"), ("webkit", "guest")]


if __name__ == "__main__":
    print(pairwise_seed())
