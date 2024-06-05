import pytest
from selenium.webdriver.common.by import By
import helpers


def test_login_from_main_page(driver, base_url, credentials):
    driver.get(base_url)

    login_button = driver.find_element(By.XPATH, "//button[text() = 'Войти в аккаунт']")
    login_button.click()

    if not helpers.wait_for_url_contains(driver, 'login'):
        pytest.fail("URL не изменился в течение 3 секунд до содержимого 'login'.")

    helpers.perform_login(driver, credentials["email"], credentials["password"])

    assert helpers.wait_for_url_change(driver, base_url + 'login'), "URL не изменился в течение 3 секунд после нажатия кнопки 'Войти'."


def test_login_from_profile_page(driver, base_url, credentials):
    driver.get(base_url)

    profile_button = driver.find_element(By.XPATH, "//a[@href = '/account']")
    profile_button.click()

    if not helpers.wait_for_url_contains(driver, 'login'):
        pytest.fail("URL не изменился в течение 3 секунд до содержимого 'login'.")

    helpers.perform_login(driver, credentials["email"], credentials["password"])

    assert helpers.wait_for_url_change(driver, base_url + 'login'), "URL не изменился в течение 3 секунд после нажатия кнопки 'Войти'."


def test_login_from_registration_page(driver, base_url, credentials):
    driver.get(base_url + 'register')

    login_button = driver.find_element(By.XPATH, "//a[@href = '/login']")
    login_button.click()

    if not helpers.wait_for_url_contains(driver, 'login'):
        pytest.fail("URL не изменился в течение 3 секунд до содержимого 'login'.")

    helpers.perform_login(driver, credentials["email"], credentials["password"])

    assert helpers.wait_for_url_change(driver, base_url + 'login'), "URL не изменился в течение 3 секунд после нажатия кнопки 'Войти'."


def test_login_from_recovery_page(driver, base_url, credentials):
    driver.get(base_url + 'forgot-password')

    login_button = driver.find_element(By.XPATH, "//a[@href = '/login']")
    login_button.click()

    if not helpers.wait_for_url_contains(driver, 'login'):
        pytest.fail("URL не изменился в течение 3 секунд до содержимого 'login'.")

    helpers.perform_login(driver, credentials["email"], credentials["password"])

    assert helpers.wait_for_url_change(driver, base_url + 'login'), "URL не изменился в течение 3 секунд после нажатия кнопки 'Войти'."