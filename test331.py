import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegistration(unittest.TestCase):
    """Класс для тестирования страниц регистрации"""
    
    def setUp(self):
        """Открываем браузер перед каждым тестом"""
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)
    
    def tearDown(self):
        """Закрываем браузер после каждого теста"""
        time.sleep(2)  # Пауза, чтобы визуально оценить результат
        self.browser.quit()
    
    def test_registration_page_1(self):
        """Тест для первой страницы регистрации"""
        # Открываем первую страницу
        self.browser.get("http://suninjuly.github.io/registration1.html")
        
        # Находим и заполняем обязательные поля
        # ВНИМАНИЕ: Селекторы нужно проверить и подставить актуальные!
        first_name = self.browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        first_name.send_keys("Ivan")
        
        last_name = self.browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        last_name.send_keys("Petrov")
        
        email = self.browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        email.send_keys("ivan.petrov@example.com")
        
        # Отправляем форму
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        
        # Ждём загрузки страницы с результатом
        time.sleep(1)
        
        # Находим элемент с текстом благодарности
        welcome_text_element = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_element.text
        
        # Проверяем, что ожидаемый текст совпадает с текстом на странице
        expected_text = "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text, expected_text, 
                         f"Ожидался текст '{expected_text}', но получен '{welcome_text}'")
    
    def test_registration_page_2(self):
        """Тест для второй страницы регистрации (где есть баг с отсутствующим полем)"""
        # Открываем вторую страницу
        self.browser.get("http://suninjuly.github.io/registration2.html")
        
        # Находим и заполняем обязательные поля
        # ВНИМАНИЕ: На этой странице может не быть какого-то поля!
        first_name = self.browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        first_name.send_keys("Ivan")
        
        last_name = self.browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        last_name.send_keys("Petrov")
        
        email = self.browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        email.send_keys("ivan.petrov@example.com")
        
        # Отправляем форму
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        
        # Ждём загрузки страницы с результатом
        time.sleep(1)
        
        # Находим элемент с текстом благодарности
        welcome_text_element = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_element.text
        
        # Проверяем, что ожидаемый текст совпадает с текстом на странице
        expected_text = "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text, expected_text, 
                         f"Ожидался текст '{expected_text}', но получен '{welcome_text}'")

if __name__ == "__main__":
    unittest.main()