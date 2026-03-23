REVIEW_STACK = ["requests", "pytest", "sqlite3", "allure"]

def show_review_stack() -> None:
    for item in REVIEW_STACK:
        print(item)

if __name__ == "__main__":
    show_review_stack()
