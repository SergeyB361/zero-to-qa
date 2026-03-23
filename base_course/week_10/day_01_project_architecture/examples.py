PORTFOLIO_STRUCTURE = [
    "tests/unit",
    "tests/api",
    "tests/ui",
    "pages",
    "clients",
    "utils",
    "data",
    "config",
]

def show_portfolio_structure() -> None:
    for item in PORTFOLIO_STRUCTURE:
        print(item)

if __name__ == "__main__":
    show_portfolio_structure()
