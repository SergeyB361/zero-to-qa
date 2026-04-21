"""
Практическое задание:
1. Сравни две версии модели по наборам колонок.
2. Верни, какие колонки добавились.
3. Не пытайся строить Alembic migration полностью — нужен только честный diff.

Например:
- old: `['id', 'name']`
- new: `['id', 'name', 'is_active']`
- result: `{'added': ['is_active'], 'removed': []}`

Критерий готовности: `run_checks()` проходит без ошибок.
"""


def diff_columns(old: list[str], new: list[str]) -> dict[str, list[str]]:
    # TODO: реализуй честный schema diff по спискам колонок.
    return {'added': [], 'removed': []}


def run_checks() -> None:
    result = diff_columns(['id', 'name'], ['id', 'name', 'is_active'])
    assert result == {'added': ['is_active'], 'removed': []}, 'migration intro practice should detect newly added column'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
