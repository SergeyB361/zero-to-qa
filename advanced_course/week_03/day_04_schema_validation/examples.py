USER_SCHEMA = {
    'required': {'id', 'email', 'role'},
    'types': {'id': int, 'email': str, 'role': str},
    'role_values': {'user', 'admin', 'guest'},
}


def validate_user_schema(payload: dict[str, object]) -> bool:
    if not USER_SCHEMA['required'].issubset(payload):
        return False
    if not isinstance(payload['id'], int):
        return False
    if not isinstance(payload['email'], str):
        return False
    return payload['role'] in USER_SCHEMA['role_values']


if __name__ == '__main__':
    print(validate_user_schema({'id': 1, 'email': 'qa@example.com', 'role': 'admin'}))
