def has_duplicate_bruteforce(items: list[int]) -> bool:
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                return True
    return False



def has_duplicate_with_set(items: list[int]) -> bool:
    seen: set[int] = set()
    for item in items:
        if item in seen:
            return True
        seen.add(item)
    return False


if __name__ == "__main__":
    sample = [1, 4, 2, 4, 9]
    print(has_duplicate_bruteforce(sample))
    print(has_duplicate_with_set(sample))
