def paginate(items: list[int], page: int, limit: int) -> list[int]:
    start = (page - 1) * limit
    end = start + limit
    return items[start:end]


def filter_even(items: list[int]) -> list[int]:
    return [item for item in items if item % 2 == 0]


if __name__ == "__main__":
    print(paginate(list(range(1, 11)), page=2, limit=3))
    print(filter_even(list(range(1, 11))))
