LOCATORS = {
    "best": "get_by_role('button', name='Save')",
    "good": "get_by_test_id('save-button')",
    "risky": "locator('div:nth-child(4) > button')",
}


if __name__ == "__main__":
    for name, locator in LOCATORS.items():
        print(name, locator)
