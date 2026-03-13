import pytest
from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    # Открыть страницу товара
    page = ProductPage(browser, link)
    page.open()

    # Нажать "Добавить в корзину"
    page.add_to_basket()

    # Решить капчу и получить код
    page.solve_quiz_and_get_code()

    # Проверить название товара
    product_name = page.get_product_name()
    message_product_name = page.get_basket_success_message()
    assert product_name == message_product_name, \
        f"Название товара '{product_name}' не совпадает с названием в сообщении '{message_product_name}'"

    # Проверить стоимость корзины
    product_price = page.get_product_price()
    basket_total = page.get_basket_total_message()
    assert product_price == basket_total, \
        f"Цена товара '{product_price}' не совпадает со стоимостью корзины '{basket_total}'"
if __name__ == "__main__":
    pytest.main(["-s", "test_product_page.py"])