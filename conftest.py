import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def base_url():
    return "https://stellarburgers.nomoreparties.site/"

@pytest.fixture
def credentials():
    return { 'name': 'test_user', 'email': 'test@domain.ru', 'password': 'test_password' }