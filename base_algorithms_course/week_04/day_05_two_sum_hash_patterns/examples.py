def two_sum_indices(items: list[int], target: int) -> tuple[int, int] | None:
    seen: dict[int, int] = {}
    for index, value in enumerate(items):
        needed = target - value
        if needed in seen:
            return seen[needed], index
        seen[value] = index
    return None



def has_pair_with_sum(items: list[int], target: int) -> bool:
    seen: set[int] = set()
    for value in items:
        if target - value in seen:
            return True
        seen.add(value)
    return False


if __name__ == "__main__":
    print(two_sum_indices([2, 7, 11, 15], 9))
    print(has_pair_with_sum([1, 4, 8, 10], 12))
