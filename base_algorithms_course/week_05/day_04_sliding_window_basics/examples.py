def max_sum_window(items: list[int], k: int) -> int:
    if k <= 0 or k > len(items):
        return 0

    current_sum = sum(items[:k])
    best_sum = current_sum

    for right in range(k, len(items)):
        current_sum += items[right]
        current_sum -= items[right - k]
        if current_sum > best_sum:
            best_sum = current_sum

    return best_sum



def window_sums(items: list[int], k: int) -> list[int]:
    if k <= 0 or k > len(items):
        return []

    result = [sum(items[:k])]
    current_sum = result[0]

    for right in range(k, len(items)):
        current_sum += items[right]
        current_sum -= items[right - k]
        result.append(current_sum)

    return result


if __name__ == "__main__":
    print(max_sum_window([2, 1, 5, 1, 3, 2], 3))
    print(window_sums([2, 1, 5, 1, 3, 2], 3))
