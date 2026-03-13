from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

# Функция решения математической задачи
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# Инициализация драйвера
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    # Явное ожидание (не меньше 12 секунд)
    wait = WebDriverWait(browser, 12)

    # Ждём, пока цена станет $100
    wait.until(
        EC.text_to_be_present_in_element(
            (By.ID, "price"),
            "$100"
        )
    )

    # Нажимаем кнопку Book
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # Получаем значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # Считаем результат
    result = calc(x)

    # Вводим ответ
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(result)

    # Отправляем форму
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

finally:
    # Небольшая пауза для просмотра результата (по желанию)
    time.sleep(5)
    browser.quit()