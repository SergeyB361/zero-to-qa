# Неделя 8, День 2 - Интервальные задачи
#
# Задание 1:
# Реализуй merge_intervals(intervals).
#
# Задание 2:
# Реализуй has_overlap(intervals).
# Считай касание по границе пересечением: (3, 4) и (4, 5) -> overlap.
#
# Задание 3:
# Реализуй insert_interval(intervals, new_interval),
# возвращающую список после вставки и merge.


def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    return []



def has_overlap(intervals: list[tuple[int, int]]) -> bool:
    return False



def insert_interval(
    intervals: list[tuple[int, int]], new_interval: tuple[int, int]
) -> list[tuple[int, int]]:
    return []


if __name__ == "__main__":
    sample = [(1, 3), (6, 9)]
    print(merge_intervals([(1, 4), (2, 5), (8, 10)]))
    print(has_overlap([(1, 2), (3, 4), (4, 5)]))
    print(insert_interval(sample, (2, 5)))
    print("Ожидается: merge_intervals = [(1, 5), (8, 10)], has_overlap = True, insert_interval = [(1, 5), (6, 9)]")
    print("Реализуй базовые interval tasks.")
