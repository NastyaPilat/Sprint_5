import random
import string
from selenium.webdriver.common.by import By
import helpers


def perform_registration(driver, name, email, password):
    [input_name, input_email, input_password] = driver.find_elements(By.TAG_NAME, "input")

    input_name.send_keys(name)
    input_email.send_keys(email)
    input_password.send_keys(password)
    
    registration_button = driver.find_element(By.XPATH, "//button[text() = 'Зарегистрироваться']")
    registration_button.click()


def test_successful_registration(driver, base_url, credentials):
    driver.get(base_url + 'register')

    email = ''.join(random.choices(string.ascii_letters, k=6)) + '@domain.ru'

    perform_registration(driver, credentials["name"], email, credentials["password"])

    assert helpers.wait_for_url_contains(driver, 'login')


def test_password_error(driver, base_url, credentials):
    driver.get(base_url + 'register')

    perform_registration(driver, credentials["name"], credentials["email"], 'r')

    input_container = driver.find_element(By.XPATH, "(//div[contains(@class, 'input__container')])[last()]")
    error_message = input_container.find_element(By.XPATH, "//p[text() = 'Некорректный пароль']")

    assert error_message is not None