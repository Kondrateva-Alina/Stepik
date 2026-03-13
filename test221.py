from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Находим числа и вычисляем сумму
    num1 = browser.find_element(By.CSS_SELECTOR, "#num1").text
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2").text
    summa = int(num1) + int(num2)

    # 2. Работа с выпадающим списком
    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(str(summa))  # Важно: передаём строку!

    # 3. Нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # 4. Получаем число из alert и выводим его
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(f"Ответ: {alert_text.split()[-1]}")
    alert.accept()

finally:
    # небольшое ожидание перед закрытием
    time.sleep(5)
    browser.quit()