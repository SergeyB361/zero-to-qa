from dataclasses import dataclass


class FakePage:
    def __init__(self) -> None:
        self.current_url = "about:blank"
        self.fields: dict[str, str] = {}
        self.clicked: list[str] = []
        self.messages: dict[str, str] = {}

    def goto(self, url: str) -> None:
        self.current_url = url

    def fill(self, locator: str, value: str) -> None:
        self.fields[locator] = value

    def click(self, locator: str) -> None:
        self.clicked.append(locator)
        if locator == "button:sign-in":
            username = self.fields.get("input:username", "")
            self.current_url = "/dashboard"
            self.messages["banner:welcome"] = f"Welcome, {username}"

    def text_content(self, locator: str) -> str:
        return self.messages.get(locator, "")


class BasePage:
    def __init__(self, page: FakePage) -> None:
        self.page = page

    def current_url(self) -> str:
        return self.page.current_url


class HeaderComponent:
    def __init__(self, page: FakePage) -> None:
        self.page = page

    def open_profile_menu(self) -> None:
        self.page.click("button:profile-menu")


class LoginPage(BasePage):
    def open(self) -> None:
        self.page.goto("/login")

    def enter_username(self, username: str) -> None:
        self.page.fill("input:username", username)

    def enter_password(self, password: str) -> None:
        self.page.fill("input:password", password)

    def submit(self) -> None:
        self.page.click("button:sign-in")


class DashboardPage(BasePage):
    def __init__(self, page: FakePage) -> None:
        super().__init__(page)
        self.header = HeaderComponent(page)

    def welcome_banner(self) -> str:
        return self.page.text_content("banner:welcome")


@dataclass
class AuthFlow:
    login_page: LoginPage
    dashboard_page: DashboardPage

    def login_as(self, username: str, password: str) -> DashboardPage:
        self.login_page.open()
        self.login_page.enter_username(username)
        self.login_page.enter_password(password)
        self.login_page.submit()
        return self.dashboard_page


if __name__ == "__main__":
    page = FakePage()
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    auth_flow = AuthFlow(login_page, dashboard_page)

    dashboard = auth_flow.login_as("qa_user", "secret")

    print("=== flow result ===")
    print("current url:", dashboard.current_url())
    print("welcome banner:", dashboard.welcome_banner())
    print()

    print("=== why this is page object architecture ===")
    print("Page object hides locators and low-level actions.")
    print("Reusable flow composes several page objects.")
    print("Assertions stay in the test layer, not inside page objects.")

    assert dashboard.current_url() == "/dashboard"
    assert dashboard.welcome_banner() == "Welcome, qa_user"