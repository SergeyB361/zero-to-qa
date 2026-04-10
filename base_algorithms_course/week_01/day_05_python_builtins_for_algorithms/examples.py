def build_frequency_map(items: list[str]) -> dict[str, int]:
    freq: dict[str, int] = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    return freq


def unique_items(items: list[int]) -> set[int]:
    return set(items)


def pair_names_and_scores(names: list[str], scores: list[int]) -> list[tuple[str, int]]:
    return list(zip(names, scores))


if __name__ == "__main__":
    print(build_frequency_map(["api", "ui", "api", "db"]))
    print(unique_items([1, 2, 2, 3, 1]))
    print(pair_names_and_scores(["ann", "bob"], [90, 85]))
