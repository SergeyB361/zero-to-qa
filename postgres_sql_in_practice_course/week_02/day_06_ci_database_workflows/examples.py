def ci_steps() -> list[str]:
    return [
        'start postgres service',
        'wait for health',
        'apply schema and seed',
        'run checks',
        'collect artifacts',
    ]


def main() -> None:
    assert len(ci_steps()) == 5
    print('CI workflow example passed')


if __name__ == '__main__':
    main()
