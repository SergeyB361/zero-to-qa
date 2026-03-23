def browser_matrix(kind: str) -> list[str]:
    if kind == "smoke":
        return ["chromium", "firefox"]
    return ["chromium", "firefox", "webkit"]


if __name__ == "__main__":
    print(browser_matrix("smoke"))
