from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import TimeoutException


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