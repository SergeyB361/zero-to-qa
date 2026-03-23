class LoginPage:
    def __init__(self, page) -> None:
        self.page = page

    def open(self) -> None:
        self.page.goto("https://example.com/login")

    def login(self, email: str, password: str) -> None:
        self.page.locator("input[name=email]").fill(email)
        self.page.locator("input[name=password]").fill(password)
