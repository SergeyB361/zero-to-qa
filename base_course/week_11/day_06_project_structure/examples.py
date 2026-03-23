PROJECT_LAYOUT = [
    "tests/unit",
    "tests/api",
    "tests/ui",
    "clients",
    "utils",
    "data",
    "pytest.ini",
    "requirements.txt",
]

def show_layout() -> None:
    for item in PROJECT_LAYOUT:
        print(item)

if __name__ == "__main__":
    show_layout()
