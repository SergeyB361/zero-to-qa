UI_REFINEMENT_AREAS = [
    "stable locators",
    "explicit assertions",
    "clear page objects",
    "less flaky waits",
]

def show_ui_refinement_areas() -> None:
    for item in UI_REFINEMENT_AREAS:
        print(item)

if __name__ == "__main__":
    show_ui_refinement_areas()
