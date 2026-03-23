def transform_requirement(requirement: str) -> dict[str, list[str]]:
    return {
        "risks": ["ambiguous behavior"],
        "tests": [f"cover requirement: {requirement}"],
    }


if __name__ == "__main__":
    print(transform_requirement("Order can be cancelled before payment"))
