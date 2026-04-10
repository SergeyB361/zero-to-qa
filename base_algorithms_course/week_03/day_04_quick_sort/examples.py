def quick_sort(items: list[int]) -> list[int]:
    if len(items) <= 1:
        return items[:]

    pivot = items[len(items) // 2]
    less = [x for x in items if x < pivot]
    equal = [x for x in items if x == pivot]
    greater = [x for x in items if x > pivot]

    return quick_sort(less) + equal + quick_sort(greater)


if __name__ == "__main__":
    print(quick_sort([10, 7, 8, 9, 1, 5]))
