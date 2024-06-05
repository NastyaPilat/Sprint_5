from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


def wait_for_url_contains(driver, substring, timeout=3):
    try:
        WebDriverWait(driver, timeout).until(EC.url_contains(substring))
        return True
    except TimeoutException:
        return False


def wait_for_url_change(driver, old_url, timeout=3):
    try:
        WebDriverWait(driver, timeout).until(EC.url_changes(old_url))
        return True
    except TimeoutException:
        return False
    

def perform_registration(driver, name, email, password):
    [input_name, input_email, input_password] = driver.find_elements(By.TAG_NAME, "input")

    input_name.send_keys(name)
    input_email.send_keys(email)
    input_password.send_keys(password)
    
    registration_button = driver.find_element(By.XPATH, "//button[text() = 'Зарегистрироваться']")
    registration_button.click()
    

def perform_login(driver, email, password):
    [input_email, input_password] = driver.find_elements(By.TAG_NAME, "input")
    
    input_email.send_keys(email)
    input_password.send_keys(password)
    
    login_button = driver.find_element(By.XPATH, "//button[text() = 'Войти']")
    login_button.click()