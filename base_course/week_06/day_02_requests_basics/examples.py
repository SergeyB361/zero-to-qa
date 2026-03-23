import requests

def get_users() -> requests.Response:
    return requests.get("https://reqres.in/api/users", timeout=10)

def create_user(payload: dict) -> requests.Response:
    return requests.post("https://reqres.in/api/users", json=payload, timeout=10)
