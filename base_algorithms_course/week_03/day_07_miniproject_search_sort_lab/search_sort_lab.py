# Неделя 3, День 7 - Мини-проект: Search and Sort Lab


def linear_search(items: list[int], target: int) -> int:
    return -1


def binary_search(items: list[int], target: int) -> int:
    return -1


def merge_sort(items: list[int]) -> list[int]:
    return []


def main() -> None:
    unsorted_items = [7, 2, 9, 1, 5]
    sorted_items = [1, 2, 5, 7, 9]

    print('Search and Sort Lab demo scaffold')
    print('merge_sort ->', merge_sort(unsorted_items), '| expected: [1, 2, 5, 7, 9]')
    print('linear_search(target=5) ->', linear_search(unsorted_items, 5), '| expected: 4 or другой корректный индекс в исходном списке')
    print('binary_search(target=7) ->', binary_search(sorted_items, 7), '| expected: 3')
    print('Финальная версия должна показывать сравнение search и sort по условиям spec.md.')


if __name__ == "__main__":
    main()
