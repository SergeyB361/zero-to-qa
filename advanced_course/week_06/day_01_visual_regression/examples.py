def snapshot_name(page_name: str, browser: str) -> str:
    return f"{page_name}-{browser}.png"


if __name__ == "__main__":
    print(snapshot_name("checkout", "chromium"))
