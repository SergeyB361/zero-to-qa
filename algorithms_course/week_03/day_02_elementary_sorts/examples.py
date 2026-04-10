def bubble_sort(items: list[int]) -> list[int]:
    arr = items[:]
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr



def selection_sort(items: list[int]) -> list[int]:
    arr = items[:]
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr



def insertion_sort(items: list[int]) -> list[int]:
    arr = items[:]
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr


if __name__ == "__main__":
    sample = [5, 1, 4, 2, 8]
    print(bubble_sort(sample))
    print(selection_sort(sample))
    print(insertion_sort(sample))
