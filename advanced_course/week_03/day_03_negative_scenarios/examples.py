def validate_create_payload(payload: dict[str, object]) -> tuple[int, str]:
    if 'email' not in payload:
        return 400, 'email is required'
    if not isinstance(payload.get('age'), int):
        return 400, 'age must be int'
    return 201, 'created'


if __name__ == '__main__':
    print(validate_create_payload({'age': 18}))
    print(validate_create_payload({'email': 'qa@example.com', 'age': '18'}))
