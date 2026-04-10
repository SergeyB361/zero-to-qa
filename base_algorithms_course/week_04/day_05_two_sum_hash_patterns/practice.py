# Неделя 4, День 5 - Hash-паттерны типа Two Sum
#
# Задание 1:
# Реализуй has_pair_with_sum(items, target).
#
# Задание 2:
# Реализуй two_sum_indices(items, target).
#
# Задание 3:
# Реализуй has_pair_with_difference(items, diff),
# которая проверяет, есть ли пара с разностью diff.


def has_pair_with_sum(items: list[int], target: int) -> bool:
    return False



def two_sum_indices(items: list[int], target: int) -> tuple[int, int] | None:
    return None



def has_pair_with_difference(items: list[int], diff: int) -> bool:
    return False


if __name__ == "__main__":
    print(has_pair_with_sum([2, 7, 11, 15], 9))
    print(two_sum_indices([2, 7, 11, 15], 26))
    print(has_pair_with_difference([1, 5, 9, 14], 4))
    print("Ожидается: has_pair_with_sum = True, two_sum_indices = (2, 3), has_pair_with_difference = True")
    print("Реализуй hash-based паттерны поиска пар.")
