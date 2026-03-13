from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Считываем значение x
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    # 2. Вводим ответ в текстовое поле
    input_answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_answer.send_keys(y)

    # 3. Отмечаем checkbox "I'm the robot"
    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robot_checkbox.click()

    # 4. Скроллим к радиобаттону, чтобы он стал видимым (перекрыт футером)
    robots_radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robots_radio)
    robots_radio.click()

    # 5. Скроллим к кнопке Submit и кликаем
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # 6. Получаем число из alert
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(f"Ответ: {alert_text.split()[-1]}")
    alert.accept()

finally:
    time.sleep(5)
    browser.quit()