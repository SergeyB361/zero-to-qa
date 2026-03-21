from playwright.sync_api import sync_playwright

def open_example_site() -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://example.com")
        print(page.title())
        browser.close()
