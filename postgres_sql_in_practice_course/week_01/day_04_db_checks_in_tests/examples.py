def row_exists(rows: list[dict], key: str, value: object) -> bool:
    return any(row.get(key) == value for row in rows)


def count_rows(rows: list[dict]) -> int:
    return len(rows)


def main() -> None:
    rows = [
        {'id': 1, 'status': 'open'},
        {'id': 2, 'status': 'closed'},
    ]
    assert row_exists(rows, 'status', 'open') is True
    assert count_rows(rows) == 2
    print('DB-check style example passed')


if __name__ == '__main__':
    main()
