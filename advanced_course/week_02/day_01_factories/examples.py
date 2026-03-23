def make_user(
    email: str = 'qa@example.com',
    role: str = 'user',
    active: bool = True,
) -> dict[str, object]:
    return {
        'email': email,
        'role': role,
        'active': active,
    }


def make_order(total: int = 100, status: str = 'new') -> dict[str, object]:
    return {
        'total': total,
        'status': status,
        'currency': 'RUB',
    }


def clone_with(data: dict[str, object], **overrides: object) -> dict[str, object]:
    result = dict(data)
    result.update(overrides)
    return result


if __name__ == '__main__':
    default_user = make_user()
    admin_user = make_user(role='admin')
    cancelled_order = clone_with(make_order(), status='cancelled')

    print(default_user)
    print(admin_user)
    print(cancelled_order)
