def age_edges() -> list[int]:
    return [17, 18, 19, 64, 65, 66]


def amount_edges() -> list[int]:
    return [0, 1, 9_999, 10_000, 10_001]


if __name__ == '__main__':
    print(age_edges())
    print(amount_edges())
