BASELINE_USER = {
    'email': 'qa@example.com',
    'role': 'user',
    'active': True,
}

ROLE_DATASETS = {
    'admin': {'role': 'admin'},
    'guest': {'role': 'guest', 'active': False},
}

EDGE_TOTALS = [0, 1, 10_000, 10_001]


def build_user(**overrides: object) -> dict[str, object]:
    result = dict(BASELINE_USER)
    result.update(overrides)
    return result


if __name__ == '__main__':
    print(build_user())
    print(build_user(**ROLE_DATASETS['admin']))
    print(EDGE_TOTALS)
