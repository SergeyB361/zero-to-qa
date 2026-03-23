def gate_passed(coverage: int, smoke_ok: bool) -> bool:
    return coverage >= 80 and smoke_ok


if __name__ == "__main__":
    print(gate_passed(82, True))
