import time
import math
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
]


@pytest.mark.parametrize("link", links)
def test_stepik_message(link):

    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, 20)

    try:
        browser.get(link)

        # логин
        wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a.navbar__auth_login"))).click()

        wait.until(EC.visibility_of_element_located(
            (By.ID, "id_login_email"))).send_keys("EMAIL")

        browser.find_element(By.ID, "id_login_password").send_keys("PASSWORD")

        browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()

        time.sleep(5)

        # если задача уже решена — нажать "Solve again"
        try:
            browser.find_element(By.CSS_SELECTOR, "button.again-btn").click()
            time.sleep(2)
        except:
            pass

        # поле ответа
        answer = wait.until(
            EC.visibility_of_element_located((By.TAG_NAME, "textarea"))
        )

        answer.clear()

        result = math.log(int(time.time()))
        answer.send_keys(str(result))

        browser.find_element(
            By.CSS_SELECTOR, "button.submit-submission").click()

        feedback = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
        ).text

        assert feedback == "Correct!", feedback

    finally:
        browser.quit()