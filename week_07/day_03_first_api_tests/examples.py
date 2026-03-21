import requests

def test_get_users_status_code() -> None:
    response = requests.get("https://reqres.in/api/users?page=2", timeout=10)
    assert response.status_code == 200

def test_get_users_contains_data() -> None:
    response = requests.get("https://reqres.in/api/users?page=2", timeout=10)
    body = response.json()
    assert "data" in body
    assert isinstance(body["data"], list)
