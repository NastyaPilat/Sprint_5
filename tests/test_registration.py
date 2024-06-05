import random
import string
from selenium.webdriver.common.by import By
import helpers


def test_successful_registration(driver, base_url, credentials):
    driver.get(base_url + 'register')

    email = ''.join(random.choices(string.ascii_letters, k=6)) + '@domain.ru'

    helpers.perform_registration(driver, credentials["name"], email, credentials["password"])

    assert helpers.wait_for_url_contains(driver, 'login')


def test_password_error(driver, base_url, credentials):
    driver.get(base_url + 'register')

    helpers.perform_registration(driver, credentials["name"], credentials["email"], 'r')

    input_container = driver.find_element(By.XPATH, "(//div[contains(@class, 'input__container')])[last()]")
    error_message = input_container.find_element(By.XPATH, "//p[text() = 'Некорректный пароль']")

    assert error_message is not None