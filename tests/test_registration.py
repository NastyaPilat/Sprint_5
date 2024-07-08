from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import constants
import locators


def test_successful_registration(driver, random_email):
    driver.get(constants.BASE_URL + 'register')
    [input_name, input_email, input_password] = driver.find_elements(By.TAG_NAME, "input")
    input_name.send_keys(constants.CREDENTIALS["name"])
    input_email.send_keys(random_email)
    input_password.send_keys(constants.CREDENTIALS["password"])
    registration_button = driver.find_element(By.XPATH, locators.REGISTRATION_BUTTON)
    registration_button.click()
    WebDriverWait(driver, 3).until(EC.url_contains('login'))
    assert 'login' in driver.current_url

def test_password_error(driver):
    driver.get(constants.BASE_URL + 'register')
    [input_name, input_email, input_password] = driver.find_elements(By.TAG_NAME, "input")
    input_name.send_keys(constants.CREDENTIALS["name"])
    input_email.send_keys(constants.CREDENTIALS["email"])
    input_password.send_keys('r')
    registration_button = driver.find_element(By.XPATH, locators.REGISTRATION_BUTTON)
    registration_button.click()
    input_container = driver.find_element(By.XPATH, locators.INPUT_CONTAINER_FOR_PASSWORD)
    error_message = input_container.find_element(By.XPATH, locators.ERROR_MESSAGE)
    assert error_message is not None