def has_duplicate(items: list[int]) -> bool:
    seen: set[int] = set()
    for item in items:
        if item in seen:
            return True
        seen.add(item)
    return False



def index_by_id(records: list[dict[str, int | str]]) -> dict[int, dict[str, int | str]]:
    result: dict[int, dict[str, int | str]] = {}
    for record in records:
        result[record["id"]] = record
    return result



def unique_words(words: list[str]) -> set[str]:
    return set(words)


if __name__ == "__main__":
    print(has_duplicate([1, 2, 3, 2]))
    print(index_by_id([{"id": 1, "name": "Ann"}, {"id": 2, "name": "Bob"}]))
    print(unique_words(["api", "ui", "api", "db"]))
