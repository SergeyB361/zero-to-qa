import pytest


def get_role_name(user: dict) -> str:
    return user["role"]


@pytest.fixture
def user_data() -> dict:
    return {"username": "anna", "role": "admin"}


def test_get_role_name(user_data: dict) -> None:
    assert get_role_name(user_data) == "admin"
