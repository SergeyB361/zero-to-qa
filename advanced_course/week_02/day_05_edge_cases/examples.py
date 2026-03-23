def is_valid_age(age: int) -> bool:
    return 18 <= age <= 65


EDGE_CASES = [17, 18, 19, 64, 65, 66]


if __name__ == "__main__":
    for value in EDGE_CASES:
        print(value, is_valid_age(value))
