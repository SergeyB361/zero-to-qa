def migration_record(name: str, applied: bool) -> dict:
    return {'name': name, 'applied': applied}


def main() -> None:
    item = migration_record('001_add_team_column', True)
    assert item['applied'] is True
    print('Migration example passed')


if __name__ == '__main__':
    main()
