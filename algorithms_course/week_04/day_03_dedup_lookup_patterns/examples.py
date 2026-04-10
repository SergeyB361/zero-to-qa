def deduplicate(items: list[int]) -> list[int]:
    return list(set(items))



def deduplicate_preserve_order(items: list[int]) -> list[int]:
    seen: set[int] = set()
    result: list[int] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result



def first_seen_indices(items: list[str]) -> dict[str, int]:
    positions: dict[str, int] = {}
    for index, item in enumerate(items):
        if item not in positions:
            positions[item] = index
    return positions


if __name__ == "__main__":
    sample = [4, 1, 4, 2, 1, 3]
    print(deduplicate(sample))
    print(deduplicate_preserve_order(sample))
    print(first_seen_indices(["api", "ui", "api", "db"]))
