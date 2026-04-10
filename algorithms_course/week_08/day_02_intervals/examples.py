def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not intervals:
        return []

    sorted_intervals = sorted(intervals)
    merged = [sorted_intervals[0]]

    for start, end in sorted_intervals[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    return merged



def has_overlap(intervals: list[tuple[int, int]]) -> bool:
    merged = merge_intervals(intervals)
    return len(merged) < len(intervals)


if __name__ == "__main__":
    sample = [(1, 3), (2, 6), (8, 10), (9, 12)]
    print(merge_intervals(sample))
    print(has_overlap(sample))
