def architecture_flags(has_logging: bool, has_retries: bool, has_timeouts: bool) -> list[str]:
    problems = []
    if not has_logging:
        problems.append("missing logging")
    if not has_retries:
        problems.append("missing retries")
    if not has_timeouts:
        problems.append("missing timeouts")
    return problems


if __name__ == "__main__":
    print(architecture_flags(True, False, False))
