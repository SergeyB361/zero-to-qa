def validate_create_user_payload(payload: dict[str, object]) -> list[str]:
    errors: list[str] = []
    if not payload.get("email"):
        errors.append("email is required")
    if payload.get("role") not in {"user", "admin"}:
        errors.append("unsupported role")
    return errors


if __name__ == "__main__":
    print(validate_create_user_payload({"role": "owner"}))
