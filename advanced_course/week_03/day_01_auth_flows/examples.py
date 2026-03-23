def auth_headers(token: str | None) -> dict[str, str]:
    if not token:
        return {}
    return {'Authorization': f'Bearer {token}'}


def can_access_admin(role: str) -> bool:
    return role == 'admin'


if __name__ == '__main__':
    print(auth_headers('valid-token'))
    print(can_access_admin('user'))
