def build_investigation_steps(title: str) -> list[str]:
    return [
        f'hypothesis: {title}',
        'collect relevant tables',
        'write focused query',
        'record findings',
    ]


def main() -> None:
    steps = build_investigation_steps('open defects are missing from report')
    assert len(steps) == 4
    print('QA investigation example passed')


if __name__ == '__main__':
    main()
