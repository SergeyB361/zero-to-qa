import os


def load_base_url() -> str:
    return os.getenv("API_BASE_URL", "https://api.example.com")


def load_token() -> str | None:
    return os.getenv("API_TOKEN")


if __name__ == "__main__":
    print(load_base_url())
    print(load_token())
