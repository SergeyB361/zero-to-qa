# Неделя 8, День 3 - Повтор: arrays и hashing
#
# Задание 1:
# Реализуй has_duplicate(items).
#
# Задание 2:
# Реализуй first_unique(items).
#
# Задание 3:
# Реализуй range_sum_query(items, queries),
# где queries - список пар (left, right).


def has_duplicate(items: list[int]) -> bool:
    return False



def first_unique(items: list[int]) -> int | None:
    return None



def range_sum_query(items: list[int], queries: list[tuple[int, int]]) -> list[int]:
    return []


if __name__ == "__main__":
    print(has_duplicate([1, 2, 3, 1]))
    print(first_unique([4, 1, 2, 1, 2]))
    print(range_sum_query([2, 5, 1, 3, 4], [(0, 2), (1, 3)]))
    print("Ожидается: has_duplicate = True, first_unique = 4, range_sum_query = [8, 9]")
    print("Реализуй mixed practice по arrays и hashing.")
