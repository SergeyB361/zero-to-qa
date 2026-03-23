def average_latency(values: list[int]) -> float:
    return sum(values) / len(values)


if __name__ == "__main__":
    print(average_latency([120, 110, 130]))
