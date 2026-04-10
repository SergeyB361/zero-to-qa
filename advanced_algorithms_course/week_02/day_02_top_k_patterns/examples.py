import heapq


def top_k_largest(items: list[int], k: int) -> list[int]:
    return heapq.nlargest(k, items)



def top_k_smallest(items: list[int], k: int) -> list[int]:
    return heapq.nsmallest(k, items)



def top_k_by_length(words: list[str], k: int) -> list[str]:
    return heapq.nlargest(k, words, key=len)


if __name__ == "__main__":
    print(top_k_largest([4, 1, 7, 2, 9, 3], 3))
    print(top_k_smallest([4, 1, 7, 2, 9, 3], 2))
    print(top_k_by_length(["api", "automation", "ui", "database"], 2))
