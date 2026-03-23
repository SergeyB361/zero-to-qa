UI_MODULES = [
    "pages/base_page.py",
    "pages/login_page.py",
    "tests/ui/test_login.py",
]

def show_ui_modules() -> None:
    for module in UI_MODULES:
        print(module)

if __name__ == "__main__":
    show_ui_modules()
