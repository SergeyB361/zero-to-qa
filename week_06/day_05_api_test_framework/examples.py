class UsersClient:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def users_url(self) -> str:
        return f"{self.base_url}/users"
