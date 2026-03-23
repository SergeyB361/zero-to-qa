USER_DATASETS = {
    'valid_user': {'email': 'qa@example.com', 'role': 'user', 'active': True},
    'blocked_user': {'email': 'blocked@example.com', 'role': 'user', 'active': False},
}

ORDER_STATUS_DATASET = ['new', 'paid', 'cancelled']


def names(dataset: dict[str, object]) -> list[str]:
    return sorted(dataset)


if __name__ == '__main__':
    print(names(USER_DATASETS))
    print(ORDER_STATUS_DATASET)
