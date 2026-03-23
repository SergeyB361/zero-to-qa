USER_SCHEMA = {
    "required": {"id", "email", "role"},
    "roles": {"user", "admin"},
}


def validate_user_schema(payload: dict[str, object]) -> bool:
    required_ok = USER_SCHEMA["required"].issubset(payload)
    role_ok = payload.get("role") in USER_SCHEMA["roles"]
    return required_ok and role_ok


if __name__ == "__main__":
    print(validate_user_schema({"id": 1, "email": "qa@example.com", "role": "admin"}))
