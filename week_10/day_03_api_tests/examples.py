API_MODULES = [
    "clients/users_client.py",
    "tests/api/test_users.py",
    "tests/api/conftest.py",
]

def show_api_modules() -> None:
    for module in API_MODULES:
        print(module)

if __name__ == "__main__":
    show_api_modules()
