ACTIONS = [
    'page.goto("https://example.com")',
    'page.get_by_role("link", name="More information").click()',
    'page.screenshot(path="page.png")',
]

def show_actions() -> None:
    for action in ACTIONS:
        print(action)

if __name__ == "__main__":
    show_actions()
