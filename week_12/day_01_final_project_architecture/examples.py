FINAL_CHECKLIST = [
    "clear folder names",
    "no duplicated helpers",
    "tests grouped by type",
    "docs are up to date",
]

def show_final_checklist() -> None:
    for item in FINAL_CHECKLIST:
        print(item)

if __name__ == "__main__":
    show_final_checklist()
