from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Заполняем текстовые поля
    first_name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    first_name.send_keys("Ivan")
    
    last_name = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    last_name.send_keys("Petrov")
    
    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email.send_keys("ivan@example.com")

    # 2. Создаем временный текстовый файл
    current_dir = os.path.abspath(os.path.dirname("C:\Users\erosc\OneDrive\Рабочий стол\Степик"))  # папка, где находится скрипт
    file_path = os.path.join(current_dir, "bio.txt")  # полный путь к файлу
    
    with open(file_path, "w") as file:
        file.write("This is my short bio for the task.")

    # 3. Загружаем файл
    file_input = browser.find_element(By.CSS_SELECTOR, "#file")
    file_input.send_keys(file_path)

    # 4. Нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # 5. Получаем число из alert
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(f"Ответ: {alert_text.split()[-1]}")
    alert.accept()

finally:
    # небольшое ожидание и закрытие
    time.sleep(5)
    browser.quit()
    # удаляем созданный файл (необязательно, но аккуратно)
    if os.path.exists(file_path):
        os.remove(file_path)