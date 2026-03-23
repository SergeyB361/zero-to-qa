def capstone_plan(scope: str, quality_bar: str) -> dict[str, str]:
    return {"scope": scope, "quality_bar": quality_bar}


if __name__ == "__main__":
    print(capstone_plan("API + UI smoke", "stable CI and clear docs"))
