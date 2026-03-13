import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

def calculate_answer():
    """Вычисление ответа для проверки"""
    return str(math.log(int(time.time())))

@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4", 
                 marks=pytest.mark.xfail(reason="Bug in promo offer4 - price calculation error")),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
])
def test_guest_can_add_product_to_basket(browser, link):
    """Тест проверяет возможность добавления товара в корзину с различными промо-акциями"""
    
    # Открываем страницу товара с промо-параметром
    browser.get(link)
    
    # Находим и нажимаем кнопку добавления в корзину
    add_to_basket_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    add_to_basket_button.click()
    
    # Обрабатываем alert с математическим выражением
    alert = browser.switch_to.alert
    alert_text = alert.text
    
    # Извлекаем число из текста alert'а
    alert_number = alert_text.split(" ")[2]
    
    # Вычисляем ответ
    answer = str(math.log(int(alert_number)))
    
    # Вводим ответ в alert
    alert.send_keys(answer)
    alert.accept()
    
    try:
        # Проверяем успешность добавления в корзину
        success_message = browser.find_element(By.CSS_SELECTOR, ".alert-success")
        assert success_message, "Сообщение об успешном добавлении не появилось"
        
        # Проверяем название товара в сообщении
        product_name = browser.find_element(By.CSS_SELECTOR, ".product_main h1").text
        basket_product_name = browser.find_element(By.CSS_SELECTOR, ".alert-success strong").text
        assert product_name == basket_product_name, f"Название товара '{product_name}' не совпадает с названием в корзине '{basket_product_name}'"
        
        # Проверяем цену товара
        product_price = browser.find_element(By.CSS_SELECTOR, ".product_main .price_color").text
        basket_price = browser.find_element(By.CSS_SELECTOR, ".alert-info .price_color").text
        assert product_price == basket_price, f"Цена товара '{product_price}' не совпадает с ценой в корзине '{basket_price}'"
        
    except Exception as e:
        print(f"Ошибка при проверке: {e}")
        raise

# Команда для запуска теста:
# pytest -v test_promo_bug.py