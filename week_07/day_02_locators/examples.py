LOCATOR_EXAMPLES = [
    'page.get_by_role("button", name="Login")',
    'page.locator("input[name=email]")',
    'page.get_by_text("Sign up")',
]

def show_locators() -> None:
    for locator in LOCATOR_EXAMPLES:
        print(locator)

if __name__ == "__main__":
    show_locators()
