def sum_divide_and_conquer(items: list[int]) -> int:
    if not items:
        return 0
    if len(items) == 1:
        return items[0]

    mid = len(items) // 2
    left_sum = sum_divide_and_conquer(items[:mid])
    right_sum = sum_divide_and_conquer(items[mid:])
    return left_sum + right_sum



def max_divide_and_conquer(items: list[int]) -> int:
    if len(items) == 1:
        return items[0]

    mid = len(items) // 2
    left_max = max_divide_and_conquer(items[:mid])
    right_max = max_divide_and_conquer(items[mid:])
    return left_max if left_max > right_max else right_max


if __name__ == "__main__":
    sample = [7, 2, 9, 1, 5, 3]
    print(sum_divide_and_conquer(sample))
    print(max_divide_and_conquer(sample))
