def frequency_map(items: list[str]) -> dict[str, int]:
    freq: dict[str, int] = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    return freq



def most_frequent(items: list[str]) -> str:
    freq = frequency_map(items)
    best_item = ""
    best_count = -1
    for item, count in freq.items():
        if count > best_count:
            best_item = item
            best_count = count
    return best_item


if __name__ == "__main__":
    words = ["api", "ui", "api", "db", "api", "ui"]
    print(frequency_map(words))
    print(most_frequent(words))
