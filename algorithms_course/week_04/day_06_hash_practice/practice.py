# Неделя 4, День 6 - Практика на hash-подходы
#
# Задание 1:
# Реализуй intersection_size(left, right).
#
# Задание 2:
# Реализуй first_unique(items).
#
# Задание 3:
# Реализуй same_multiset(left, right),
# которая проверяет, совпадают ли два списка по составу и кратности элементов.


def intersection_size(left: list[int], right: list[int]) -> int:
    return -1



def first_unique(items: list[int]) -> int | None:
    return None



def same_multiset(left: list[int], right: list[int]) -> bool:
    return False


if __name__ == "__main__":
    print(intersection_size([1, 2, 3], [2, 3, 4]))
    print(first_unique([9, 1, 2, 1, 2]))
    print(same_multiset([1, 2, 2, 3], [2, 1, 3, 2]))
    print("Ожидается: intersection_size = 2, first_unique = 9, same_multiset = True")
    print("Реализуй смешанные задачи на dict и set.")
