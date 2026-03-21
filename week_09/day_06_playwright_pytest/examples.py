def test_example_title(page) -> None:
    page.goto("https://example.com")
    assert "Example" in page.title()
