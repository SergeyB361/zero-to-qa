def build_prefix_sums(items: list[int]) -> list[int]:
    prefix: list[int] = []
    total = 0
    for item in items:
        total += item
        prefix.append(total)
    return prefix



def range_sum(prefix: list[int], left: int, right: int) -> int:
    if left == 0:
        return prefix[right]
    return prefix[right] - prefix[left - 1]


if __name__ == "__main__":
    items = [2, 5, 1, 3, 4]
    prefix = build_prefix_sums(items)
    print(prefix)
    print(range_sum(prefix, 1, 3))
