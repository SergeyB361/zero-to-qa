def build_test_user_payload(user_id: int) -> dict:
    return {'id': user_id, 'name': f'test-user-{user_id}', 'team': 'qa'}


def cleanup_ids(created_ids: list[int]) -> list[int]:
    return sorted(created_ids)


def main() -> None:
    payload = build_test_user_payload(101)
    assert payload['id'] == 101
    assert cleanup_ids([3, 1, 2]) == [1, 2, 3]
    print('Setup/cleanup example passed')


if __name__ == '__main__':
    main()
