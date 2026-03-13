from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # Для регистрации на первой странице
    # link = "http://suninjuly.github.io/registration1.html"
    
    # Для проверки бага на второй странице
    link = "http://suninjuly.github.io/registration2.html"
    
    browser = webdriver.Chrome()
    browser.get(link)

    input_first = browser.find_element(By.CSS_SELECTOR, ".first[required]")
    input_first.send_keys("Ivan")
    
    input_last = browser.find_element(By.CSS_SELECTOR, ".second[required]")
    input_last.send_keys("Petrov")
    
    input_email = browser.find_element(By.CSS_SELECTOR, ".third[required]")
    input_email.send_keys("ivan@example.com")
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()