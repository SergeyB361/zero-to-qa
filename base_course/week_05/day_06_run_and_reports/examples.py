COMMANDS = [
    "pytest",
    "pytest -v",
    "pytest -k login",
    "pytest --tb=short",
]


def show_commands() -> None:
    for command in COMMANDS:
        print(command)


if __name__ == "__main__":
    show_commands()
