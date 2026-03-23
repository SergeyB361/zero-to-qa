def pipeline_steps() -> list[str]:
    return ["setup", "lint", "unit", "api", "ui-smoke", "artifacts"]


if __name__ == "__main__":
    print(pipeline_steps())
