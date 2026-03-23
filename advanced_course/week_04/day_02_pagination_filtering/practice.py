# День 2 — Практика: pagination и filtering

def paginate(items: list[int], page: int, limit: int) -> list[int]:
    start = 0
    end = 0
    return items[start:end]


def filter_by_min(items: list[int], min_value: int) -> list[int]:
    return []


def run_checks() -> list[tuple[str, bool]]:
    items = [1, 2, 3, 4, 5, 6]
    return [
        ('page 1 size 2', paginate(items, page=1, limit=2) == [1, 2]),
        ('page 2 size 2', paginate(items, page=2, limit=2) == [3, 4]),
        ('page 3 size 2', paginate(items, page=3, limit=2) == [5, 6]),
        ('filter by min keeps tail', filter_by_min(items, 4) == [4, 5, 6]),
    ]


if __name__ == '__main__':
    print('Добавь pagination и filter logic:')
    for name, status in run_checks():
        print(f'{name}: {status}')
