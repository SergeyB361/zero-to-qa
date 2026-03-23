def trace_row(requirement: str, tests: list[str]) -> dict[str, object]:
    return {"requirement": requirement, "tests": tests}


if __name__ == "__main__":
    print(trace_row("REQ-1", ["test_order_create", "test_order_cancel"]))
