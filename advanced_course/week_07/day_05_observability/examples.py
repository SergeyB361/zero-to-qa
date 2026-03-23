def build_observability_event(test_name: str, trace_id: str) -> dict[str, str]:
    return {"test": test_name, "trace_id": trace_id, "level": "error"}


if __name__ == "__main__":
    print(build_observability_event("test_checkout", "abc-123"))
