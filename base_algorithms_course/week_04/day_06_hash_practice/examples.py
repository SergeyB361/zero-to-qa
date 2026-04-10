def intersection_size(left: list[int], right: list[int]) -> int:
    return len(set(left) & set(right))



def first_unique(items: list[int]) -> int | None:
    freq: dict[int, int] = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    for item in items:
        if freq[item] == 1:
            return item
    return None


if __name__ == "__main__":
    print(intersection_size([1, 2, 3, 4], [3, 4, 5]))
    print(first_unique([4, 1, 2, 1, 2, 5]))
