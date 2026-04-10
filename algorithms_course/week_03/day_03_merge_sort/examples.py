def merge(left: list[int], right: list[int]) -> list[int]:
    result: list[int] = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result



def merge_sort(items: list[int]) -> list[int]:
    if len(items) <= 1:
        return items[:]

    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    return merge(left, right)


if __name__ == "__main__":
    sample = [8, 3, 5, 4, 7, 6, 1, 2]
    print(merge([1, 4, 7], [2, 3, 6]))
    print(merge_sort(sample))
