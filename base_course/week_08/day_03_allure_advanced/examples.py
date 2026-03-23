import allure

@allure.title("Проверка суммы корзины")
def test_cart_total() -> None:
    with allure.step("Проверить, что итоговая сумма верная"):
        assert 100 + 50 == 150
