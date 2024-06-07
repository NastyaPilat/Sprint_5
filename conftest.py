import pytest
from selenium import webdriver
import random
import string


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def random_email():
    return ''.join(random.choices(string.ascii_letters, k=6)) + '@domain.ru'
