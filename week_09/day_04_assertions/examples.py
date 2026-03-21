from playwright.sync_api import expect

def example_assertions(page) -> None:
    expect(page).to_have_url("https://example.com/")
    expect(page.get_by_role("heading")).to_be_visible()
