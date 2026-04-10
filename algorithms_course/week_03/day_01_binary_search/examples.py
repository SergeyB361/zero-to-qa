def binary_search(items: list[int], target: int) -> int:
    left = 0
    right = len(items) - 1

    while left <= right:
        mid = (left + right) // 2
        if items[mid] == target:
            return mid
        if items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1



def insertion_position(items: list[int], target: int) -> int:
    left = 0
    right = len(items)

    while left < right:
        mid = (left + right) // 2
        if items[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


if __name__ == "__main__":
    data = [3, 7, 10, 14, 19, 25, 31]
    print(binary_search(data, 19))
    print(binary_search(data, 8))
    print(insertion_position(data, 8))
