def classify_seed(kind: str) -> str:
    mapping = {
        'global': 'shared baseline dataset',
        'test': 'scenario-specific setup',
        'rollback': 'transaction-scoped data',
    }
    return mapping[kind]


def main() -> None:
    assert classify_seed('global') == 'shared baseline dataset'
    print('Fixture/seed strategy example passed')


if __name__ == '__main__':
    main()
