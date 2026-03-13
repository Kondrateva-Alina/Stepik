from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Находим картинку-сундук
    treasure_img = browser.find_element(By.CSS_SELECTOR, "img#treasure")
    
    # 2. Берём значение атрибута valuex
    x = treasure_img.get_attribute("valuex")
    
    # 3. Вычисляем функцию
    y = calc(x)

    # 4. Вводим ответ в текстовое поле
    input_answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_answer.send_keys(y)

    # 5. Отмечаем checkbox "I'm the robot"
    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robot_checkbox.click()

    # 6. Выбираем radiobutton "Robots rule!"
    robots_radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    robots_radio.click()

    # 7. Нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы скопировать код ответа
    time.sleep(30)
    browser.quit()