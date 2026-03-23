def age_class(value: int) -> str:
    if value < 18:
        return "too_low"
    if value <= 65:
        return "valid"
    return "too_high"


if __name__ == "__main__":
    for value in [17, 18, 65, 66]:
        print(value, age_class(value))
