import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_guest_should_see_add_to_basket_button(browser):
    """Тест проверяет наличие кнопки добавления в корзину"""
    
    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    # Даём время посмотреть на страницу (30 секунд)
    time.sleep(30)
    
    # Ищем кнопку добавления в корзину
    try:
        add_to_basket_button = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket"))
        )
    except:
        add_to_basket_button = None
    
    # Проверяем, что кнопка найдена
    assert add_to_basket_button is not None, \
        "Кнопка добавления в корзину не найдена на странице"
    
    # Проверяем, что кнопка видима
    assert add_to_basket_button.is_displayed(), \
        "Кнопка добавления в корзину найдена, но не видна на странице"
    
    # Выводим текст кнопки
    print(f"\n✅ Текст кнопки: {add_to_basket_button.text}")