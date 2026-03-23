def paginate(items: list[int], page: int, limit: int) -> list[int]:
    start = (page - 1) * limit
    end = start + limit
    return items[start:end]


def filter_by_min(items: list[int], min_value: int) -> list[int]:
    return [item for item in items if item >= min_value]


if __name__ == '__main__':
    print(paginate([1, 2, 3, 4, 5], page=2, limit=2))
    print(filter_by_min([1, 2, 3, 4, 5], 4))
