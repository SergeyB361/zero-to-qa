def choose_lookup_method(sorted_input: bool) -> str:
    if sorted_input:
        return "binary_search"
    return "linear_search"



def sort_and_deduplicate(items: list[int]) -> list[int]:
    return sorted(set(items))



def top_three(items: list[int]) -> list[int]:
    return sorted(items, reverse=True)[:3]


if __name__ == "__main__":
    print(choose_lookup_method(True))
    print(sort_and_deduplicate([4, 1, 4, 2, 2, 9]))
    print(top_three([5, 1, 7, 3, 9, 2]))
