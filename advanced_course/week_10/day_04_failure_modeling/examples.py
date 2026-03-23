def failure_modes(component: str) -> list[str]:
    return [f"{component}: timeout", f"{component}: unavailable", f"{component}: invalid response"]


if __name__ == "__main__":
    print(failure_modes("database"))
