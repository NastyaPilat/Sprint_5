from selenium.webdriver.common.by import By


def test_bun_tab(driver, base_url):
    driver.get(base_url)

    bun_tab = driver.find_element(By.XPATH, "//div[span[text() = 'Булки']]")
    sauce_tab = driver.find_element(By.XPATH, "//div[span[text() = 'Соусы']]")

    sauce_tab.click()
    bun_tab.click()

    assert 'tab_tab_type_current__2BEPc' in bun_tab.get_attribute('class')


def test_sauce_tab(driver, base_url):
    driver.get(base_url)

    sauce_tab = driver.find_element(By.XPATH, "//div[span[text() = 'Соусы']]")

    sauce_tab.click()

    assert 'tab_tab_type_current__2BEPc' in sauce_tab.get_attribute('class')


def test_topping_tab(driver, base_url):
    driver.get(base_url)

    topping_tab = driver.find_element(By.XPATH, "//div[span[text() = 'Начинки']]")

    topping_tab.click()

    assert 'tab_tab_type_current__2BEPc' in topping_tab.get_attribute('class')