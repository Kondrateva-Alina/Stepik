from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        add_button.click()

    def get_product_name(self):
        product_name = self.browser.find_element(By.CSS_SELECTOR, "div.product_main h1").text
        return product_name

    def get_product_price(self):
        product_price = self.browser.find_element(By.CSS_SELECTOR, "p.price_color").text
        return product_price

    def get_basket_success_message(self):
        message = self.browser.find_element(By.CSS_SELECTOR, "div.alertinner strong").text
        return message

    def get_basket_total_message(self):
        # Ищем второе сообщение с ценой
        basket_total = self.browser.find_elements(By.CSS_SELECTOR, "div.alertinner p strong")[1].text
        return basket_total