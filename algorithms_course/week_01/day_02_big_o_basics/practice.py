# Неделя 1, День 2 - Сложность: Big O
#
# Задание 1:
# Реализуй функцию get_last_item(items) и подпиши её сложность.
#
# Задание 2:
# Реализуй функцию count_zeros(items) и подпиши её сложность.
#
# Задание 3:
# Посмотри на функцию has_pair_sum_bruteforce и подпиши её сложность.


def get_last_item(items: list[int]) -> int:
    # TODO: O(?)
    return -1



def count_zeros(items: list[int]) -> int:
    # TODO: O(?)
    return -1



def has_pair_sum_bruteforce(items: list[int], target: int) -> bool:
    # TODO: подпиши сложность O(?)
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] + items[j] == target:
                return True
    return False


if __name__ == "__main__":
    sample = [1, 0, 3, 0, 5]
    print(get_last_item(sample))
    print(count_zeros(sample))
    print(has_pair_sum_bruteforce([2, 7, 11, 15], 9))
    print("Ожидается: get_last_item = 5, count_zeros = 2, has_pair_sum_bruteforce = True")
    print("Реализуй функции и подпиши сложности в комментариях.")
