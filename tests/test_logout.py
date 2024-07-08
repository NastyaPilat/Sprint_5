from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import constants
import locators


def test_logout_from_main_page(driver):
    driver.get(constants.BASE_URL + 'login')
    [input_email, input_password] = driver.find_elements(By.TAG_NAME, "input")
    input_email.send_keys(constants.CREDENTIALS["email"])
    input_password.send_keys(constants.CREDENTIALS["password"])
    login_button = driver.find_element(By.XPATH, locators.LOGIN_BUTTON_ON_LOGIN_PAGE)
    login_button.click()
    WebDriverWait(driver, 3).until(EC.url_changes(constants.BASE_URL + 'login'))
    profile_button = driver.find_element(By.XPATH, locators.PROFILE_BUTTON)
    profile_button.click()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, locators.LOGOUT_BUTTON)))
    logout_button = driver.find_element(By.XPATH, locators.LOGOUT_BUTTON)
    logout_button.click()
    WebDriverWait(driver, 3).until(EC.url_contains('login'))
    assert 'login' in driver.current_url