def validate_user(user: dict) -> None:
    assert "id" in user
    assert "email" in user
    assert isinstance(user["id"], int)
    assert isinstance(user["email"], str)
