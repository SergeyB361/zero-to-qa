def get_first_item(items: list[int]) -> int:
    return items[0]  # O(1)


def contains_zero(items: list[int]) -> bool:
    for item in items:  # O(n)
        if item == 0:
            return True
    return False


def has_duplicate_pair(items: list[int]) -> bool:
    for i in range(len(items)):  # O(n^2)
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                return True
    return False


if __name__ == "__main__":
    data = [4, 2, 0, 9]
    print(get_first_item(data))
    print(contains_zero(data))
    print(has_duplicate_pair([1, 2, 3, 1]))
