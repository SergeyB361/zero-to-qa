def wait_for(condition_values: list[bool]) -> bool:
    for value in condition_values:
        if value:
            return True
    return False


if __name__ == "__main__":
    print(wait_for([False, False, True]))
