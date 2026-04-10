def has_duplicate(items: list[int]) -> bool:
    seen: set[int] = set()
    for item in items:
        if item in seen:
            return True
        seen.add(item)
    return False



def range_sum(items: list[int], left: int, right: int) -> int:
    prefix: list[int] = []
    total = 0
    for item in items:
        total += item
        prefix.append(total)
    if left == 0:
        return prefix[right]
    return prefix[right] - prefix[left - 1]


if __name__ == "__main__":
    print(has_duplicate([1, 2, 3, 1]))
    print(range_sum([2, 5, 1, 3, 4], 1, 3))
