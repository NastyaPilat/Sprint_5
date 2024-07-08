from selenium.webdriver.common.by import By
from constants import BASE_URL
import locators


def test_bun_tab(driver):
    driver.get(BASE_URL)
    bun_tab = driver.find_element(By.XPATH, locators.BUN_TAB)
    sauce_tab = driver.find_element(By.XPATH, locators.SAUCE_TAB)
    sauce_tab.click()
    bun_tab.click()
    assert 'tab_tab_type_current__2BEPc' in bun_tab.get_attribute('class')

def test_sauce_tab(driver):
    driver.get(BASE_URL)
    sauce_tab = driver.find_element(By.XPATH, locators.SAUCE_TAB)
    sauce_tab.click()
    assert 'tab_tab_type_current__2BEPc' in sauce_tab.get_attribute('class')

def test_topping_tab(driver):
    driver.get(BASE_URL)
    topping_tab = driver.find_element(By.XPATH, locators.TOPPING_TAB)
    topping_tab.click()
    assert 'tab_tab_type_current__2BEPc' in topping_tab.get_attribute('class')