from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Нажимаем кнопку "I want to go on a magical journey!"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # 2. Переключаемся на новую вкладку
    # Запоминаем текущую вкладку
    current_window = browser.current_window_handle
    # Получаем список всех открытых вкладок
    all_windows = browser.window_handles
    # Переключаемся на новую вкладку (последнюю в списке)
    for window in all_windows:
        if window != current_window:
            browser.switch_to.window(window)
            break

    # 3. На новой вкладке решаем капчу для роботов
    # Считываем значение x
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    # Вводим ответ
    input_answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_answer.send_keys(y)

    # Нажимаем кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    # 4. Получаем число из alert и выводим его
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(f"Ответ: {alert_text.split()[-1]}")  # Извлекаем число
    alert.accept()

finally:
    # Небольшая пауза, чтобы увидеть результат
    time.sleep(5)
    browser.quit()