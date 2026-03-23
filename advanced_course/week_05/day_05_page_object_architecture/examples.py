class LoginPage:
    def __init__(self, page_title: str) -> None:
        self.page_title = page_title

    def open(self) -> str:
        return f"open:{self.page_title}"

    def login(self, username: str) -> str:
        return f"login:{username}"


if __name__ == "__main__":
    page = LoginPage("Login")
    print(page.open())
    print(page.login("qa_user"))
