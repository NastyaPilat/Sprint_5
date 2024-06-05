import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import helpers


def test_login_from_main_page(driver, base_url, credentials):
    driver.get(base_url + 'login')

    helpers.perform_login(driver, credentials["email"], credentials["password"])

    if not helpers.wait_for_url_change(driver, base_url + 'login'):
        pytest.fail("URL не изменился в течение 3 секунд после входа.")

    profile_button = driver.find_element(By.XPATH, "//a[@href = '/account']")
    profile_button.click()

    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//button[text() = 'Выход']")))

    logout_button = driver.find_element(By.XPATH, "//button[text() = 'Выход']")
    logout_button.click()

    assert helpers.wait_for_url_contains(driver, 'login'), "URL не изменился в течение 3 секунд до содержимого 'login'."