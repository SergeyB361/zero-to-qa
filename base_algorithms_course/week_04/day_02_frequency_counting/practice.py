# Неделя 4, День 2 - Подсчёт частот
#
# Задание 1:
# Реализуй frequency_map(items).
#
# Задание 2:
# Реализуй count_distinct(items).
#
# Задание 3:
# Реализуй most_frequent_number(items).


def frequency_map(items: list[int]) -> dict[int, int]:
    return {}



def count_distinct(items: list[int]) -> int:
    return -1



def most_frequent_number(items: list[int]) -> int:
    return -1


if __name__ == "__main__":
    sample = [4, 1, 4, 2, 1, 4]
    print(frequency_map(sample))
    print(count_distinct(sample))
    print(most_frequent_number(sample))
    print("Ожидается: frequency_map = {4: 3, 1: 2, 2: 1}, count_distinct = 3, most_frequent_number = 4")
    print("Реализуй frequency counting через dict.")
