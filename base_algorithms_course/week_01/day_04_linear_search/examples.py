def contains_value(items: list[int], target: int) -> bool:
    for item in items:
        if item == target:
            return True
    return False


def find_index(items: list[int], target: int) -> int:
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1


def find_all_indices(items: list[int], target: int) -> list[int]:
    result = []
    for index, item in enumerate(items):
        if item == target:
            result.append(index)
    return result


if __name__ == "__main__":
    data = [7, 3, 9, 3, 5]
    print(contains_value(data, 9))
    print(find_index(data, 3))
    print(find_all_indices(data, 3))
