# Неделя 3, День 1 - Бинарный поиск
#
# Задание 1:
# Реализуй binary_search(items, target) -> индекс элемента или -1.
#
# Задание 2:
# Реализуй contains_sorted(items, target) -> True/False через бинарный поиск.
#
# Задание 3:
# Реализуй leftmost_position(items, target) -> индекс первого target,
# если элемент встречается несколько раз.


def binary_search(items: list[int], target: int) -> int:
    return -1



def contains_sorted(items: list[int], target: int) -> bool:
    return False



def leftmost_position(items: list[int], target: int) -> int:
    return -1


if __name__ == "__main__":
    sample = [1, 2, 4, 4, 4, 7, 9]
    print(binary_search(sample, 7))
    print(contains_sorted(sample, 3))
    print(leftmost_position(sample, 4))
    print("Реализуй функции бинарного поиска.")
